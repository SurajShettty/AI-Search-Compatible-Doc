#!/usr/bin/env python3
"""
outline_sync_new.py
-------------------
One-shot sync: detects NEW source documents by ID list, AI-transforms them
via Claude CLI, and creates them in the target collection under the correct
parent tree (using id_mapping).

Run manually every 10-12 days.

Env vars:
  OUTLINE_API_TOKEN
  SOURCE_COLLECTION_IDS   comma-separated
  TARGET_COLLECTION_ID
  OUTLINE_BASE_URL        default: https://app.getoutline.com/api
  CLAUDE_CLI_PATH         default: claude
  STATE_FILE              default: outline_sync_state.json
  TITLE_PREFIX            default: [AI]
  DRY_RUN                 default: false
"""

from __future__ import annotations

import json
from dotenv import load_dotenv
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

import requests
load_dotenv() 
# ----------------------------- CONFIG -----------------------------"

API_TOKEN = os.getenv("OUTLINE_API_TOKEN", "")
SOURCE_COLLECTION_IDS = [c.strip() for c in os.getenv("SOURCE_COLLECTION_IDS", "046cc88e-b8cc-44cb-a670-75ab40030e6f").split(",") if c.strip()]
TARGET_COLLECTION_ID = os.getenv("TARGET_COLLECTION_ID", "83fe623e-b90c-4ae2-9760-873f3162aecc")
BASE_URL = os.getenv("OUTLINE_BASE_URL", "https://app.getoutline.com/api").rstrip("/")
CLAUDE_CLI = os.getenv("CLAUDE_CLI_PATH", "claude")
STATE_FILE = Path(os.getenv("STATE_FILE", "outline_sync_state.json"))
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
TITLE_PREFIX = os.getenv("TITLE_PREFIX", "[AI] ")

CLAUDE_TIMEOUT = 600
CLAUDE_RETRIES = 2
CLAUDE_MODEL = "sonnet"

SYSTEM_PROMPT = """You are a documentation transformer for a RAG (retrieval-augmented generation) chatbot that answers user questions about the Digii campus-management platform (LMS / admin / HR / academics).

Your job: take a raw Markdown document describing features and emit ONE JSON object with rich, search-optimised content.

OUTPUT SCHEMA (return JSON only — no prose, no code fences):
{
  "doc": {
    "title": "string",
    "module": "string (e.g. 'Staff Management', 'Admissions', 'EMS', 'CHC')",
    "summary": "1-3 sentence overview of the document",
    "prerequisites": [
      {"name": "string", "description": "string"}
    ],
    "tags": ["string", ...]
  },
  "chunks": [
    {
      "id": "kebab-case-unique-id",
      "feature_name": "human-readable feature name",
      "category": "sub-area within module",
      "what_it_does": "Plain-language 1-3 sentence description.",
      "why_it_matters": "Business value, 1-3 sentences.",
      "how_to_use": ["Step 1...", "Step 2...", ...],
      "examples": ["Concrete example narrative 1", "..."],
      "keywords": ["15-25 search terms incl. synonyms, action verbs, abbreviations, singular+plural forms"],
      "synonyms": ["alternate terms users may type"],
      "user_questions": [
        "5-12 realistic user questions this chunk answers, phrased naturally",
        "How do I ...?", "Can I ...?", "What happens when ...?"
      ],
      "related_features": ["ids of other chunks in this doc that connect"],
      "tags": ["topical tags"]
    }
  ]
}

RULES:
1. Clean encoding artefacts. Common mojibake patterns to fix:
   - 'â' or 'â' followed by garbage -> em dash '—'
   - 'â' -> '’' apostrophe
   - 'â' / 'â' -> curly quotes
   - stray 'Â' bytes -> remove
   Normalise to clean unicode.
2. Expand acronyms the first time they appear in a chunk (HR -> Human Resources (HR), EMS -> Examination Management System (EMS), CHC -> Campus Help Centre (CHC), LMS, KPI, OBE, DAG, REC).
3. Keywords must aggressively cover the search space:
   - feature name + variants (e.g. 'staff', 'employee', 'faculty', 'teacher', 'employees')
   - action verbs (add, create, register, onboard, edit, update, modify, deactivate, disable, suspend, download, export)
   - user roles (HR admin, registrar, super admin, principal)
   - common misspellings and informal phrasings ('staff acc', 'emp record')
   - related noun forms (bulk upload, excel template, csv, account creation)
4. user_questions must read like real chatbot queries — short, conversational, sometimes incomplete.
   Good: "How do I add 50 staff at once?", "Why can't a deactivated staff log in?"
   Bad:  "What is the functionality for performing bulk creation of staff records?"
5. Each chunk is SELF-CONTAINED. A retrieval system pulling a single chunk should let the model answer related questions without seeing siblings.
6. Preserve any numbered step lists exactly — these are how-to procedures users need verbatim.
7. If the source has tables, treat each row as a candidate chunk; merge only if rows clearly describe the same feature.
8. Do not invent functionality. If a field is empty in the source, leave the corresponding output field as an empty array/string rather than fabricating content.
9. Return ONLY the JSON object. No commentary, no markdown fences."""


# ----------------------------- OUTLINE CLIENT -----------------------------"

class OutlineClient:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    def post(self, endpoint: str, payload: dict) -> dict:
        url = f"{self.base_url}/{endpoint}"
        resp = self.session.post(url, json=payload)
        if resp.status_code == 429:
            print("    [!] Rate limited (429). Backing off 10s...", file=sys.stderr)
            time.sleep(10)
            resp = self.session.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()


# ----------------------------- STATE -----------------------------"

def load_state() -> dict:
    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
        data.setdefault("seen_source_ids", [])
        data.setdefault("id_mapping", {})
        return data
    return {"seen_source_ids": [], "id_mapping": {}}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


# ----------------------------- DOCUMENT FETCH -----------------------------"

def fetch_all_docs(client: OutlineClient, collection_id: str) -> dict[str, dict]:
    """Return dict of id -> doc for all docs in collection."""
    docs = {}
    offset = 0
    while True:
        resp = client.post("documents.list", {
            "collectionId": collection_id,
            "limit": 100,
            "offset": offset,
            "sort": "createdAt",
            "direction": "ASC",
            "statusFilter": ["published", "draft"],
        })
        batch = resp.get("data", [])
        if not batch:
            break
        for d in batch:
            docs[d["id"]] = d
        if len(batch) < 100:
            break
        offset += 100
    return docs


def get_document_info(client: OutlineClient, doc_id: str) -> dict:
    resp = client.post("documents.info", {"id": doc_id})
    return resp.get("data", {})


def get_document_text(client: OutlineClient, doc_id: str) -> str:
    resp = client.post("documents.export", {"id": doc_id})
    data = resp.get("data", {})

    # documents.export returns the markdown as a plain string.
    if isinstance(data, str):
        return data

    for key in ("text", "content", "markdown", "body"):
        if key in data and data[key]:
            return str(data[key])

    if "url" in data and data["url"]:
        r = requests.get(data["url"], timeout=30)
        r.raise_for_status()
        return r.text

    if "document" in data:
        doc = data["document"]
        for key in ("text", "content", "markdown"):
            if key in doc and doc[key]:
                return str(doc[key])

    info = get_document_info(client, doc_id)
    return info.get("text", "") or info.get("content", "") or ""


# ----------------------------- CLAUDE TRANSFORM -----------------------------"

def _find_claude() -> str:
    for name in (CLAUDE_CLI, "claude.cmd", "claude.exe", "claude"):
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError(
        "`claude` CLI not found. Install:\n"
        "    npm install -g @anthropic-ai/claude-code\n"
        "then run `claude` once to authenticate."
    )


def _extract_json(raw: str) -> dict[str, Any]:
    raw = raw.strip()
    fence = re.match(r"^```(?:json)?\s*(.*?)\s*```$", raw, re.DOTALL)
    if fence:
        raw = fence.group(1)
    start = raw.find("{")
    end = raw.rfind("}")
    if start == -1 or end == -1:
        raise json.JSONDecodeError("no JSON object found", raw, 0)
    return json.loads(raw[start : end + 1])


def render_markdown(data: dict[str, Any]) -> str:
    doc = data.get("doc", {})
    chunks = data.get("chunks", [])
    out = []

    out.append(f"# {doc.get('title', 'Untitled')}\n")
    if doc.get("module"):
        out.append(f"**Module:** {doc['module']}  ")
    if doc.get("tags"):
        out.append(f"**Tags:** {', '.join(doc['tags'])}\n")
    out.append("")

    if doc.get("summary"):
        out.append("## Overview\n")
        out.append(doc["summary"] + "\n")

    if doc.get("prerequisites"):
        out.append("## Prerequisites\n")
        for p in doc["prerequisites"]:
            if isinstance(p, dict):
                out.append(f"- **{p.get('name', '')}** — {p.get('description', '')}")
            else:
                out.append(f"- {p}")
        out.append("")

    for ch in chunks:
        out.append(f"## {ch.get('feature_name', ch.get('id', 'Feature'))}\n")
        out.append(f"<!-- id: {ch.get('id', '')} | category: {ch.get('category', '')} -->\n")

        if ch.get("what_it_does"):
            out.append("**What it does**\n")
            out.append(ch["what_it_does"] + "\n")

        if ch.get("why_it_matters"):
            out.append("**Why it matters**\n")
            out.append(ch["why_it_matters"] + "\n")

        if ch.get("how_to_use"):
            out.append("**How to use**\n")
            for i, step in enumerate(ch["how_to_use"], 1):
                out.append(f"{i}. {step}")
            out.append("")

        if ch.get("examples"):
            out.append("**Examples**\n")
            for ex in ch["examples"]:
                out.append(f"- {ex}")
            out.append("")

        if ch.get("user_questions"):
            out.append("**Questions this answers**\n")
            for q in ch["user_questions"]:
                out.append(f"- {q}")
            out.append("")

        if ch.get("keywords"):
            out.append(f"**Keywords:** {', '.join(ch['keywords'])}\n")
        if ch.get("synonyms"):
            out.append(f"**Synonyms:** {', '.join(ch['synonyms'])}\n")
        if ch.get("related_features"):
            out.append(f"**Related:** {', '.join(ch['related_features'])}\n")
        if ch.get("tags"):
            out.append(f"**Tags:** {', '.join(ch['tags'])}\n")
        out.append("---\n")

    return "\n".join(out)


def transform_document(title: str, markdown: str) -> str:
    claude_path = _find_claude()
    fd, sys_prompt_file = tempfile.mkstemp(prefix="outline_sys_", suffix=".txt", text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(SYSTEM_PROMPT)

        user_msg = (
            f"Source filename: {title}.md\n"
            f"Module hint: \n\n"
            f"--- BEGIN DOCUMENT ---\n{markdown}\n--- END DOCUMENT ---"
        )

        cmd = [
            claude_path,
            "-p",
            "--model", CLAUDE_MODEL,
            "--system-prompt-file", sys_prompt_file,
            "--output-format", "text",
        ]

        last_err = None
        for attempt in range(1, CLAUDE_RETRIES + 1):
            try:
                result = subprocess.run(
                    cmd,
                    input=user_msg,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=CLAUDE_TIMEOUT,
                )
                if result.returncode != 0:
                    raise RuntimeError(
                        f"claude CLI exit {result.returncode}: {result.stderr.strip()[:500]}"
                    )
                data = _extract_json(result.stdout)
                return render_markdown(data)

            except (RuntimeError, json.JSONDecodeError, subprocess.TimeoutExpired) as e:
                last_err = e
                wait = 2 ** attempt
                print(f"  ! Claude attempt {attempt} failed ({e.__class__.__name__}); retry in {wait}s", file=sys.stderr)
                time.sleep(wait)

        raise RuntimeError(f"Transform failed after {CLAUDE_RETRIES}: {last_err}")
    finally:
        try:
            os.unlink(sys_prompt_file)
        except OSError:
            pass


# ----------------------------- TREE / CREATE LOGIC -----------------------------"

_processing_stack: set[str] = set()


def resolve_target_parent(
    client: OutlineClient,
    source_parent_id: str | None,
    state: dict,
) -> str | None:
    """
    Return the target document ID to use as parent.
    If the source parent is unmapped but unseen, process it first (recursive).
    """
    if not source_parent_id:
        return None

    # Already mapped from a previous run
    if source_parent_id in state["id_mapping"]:
        return state["id_mapping"][source_parent_id]

    # Parent is unseen — process it now
    if source_parent_id not in state["seen_source_ids"]:
        print(f"    [tree] Parent {source_parent_id} not yet in target. Creating ancestor first...")
        target_id = process_source_document(client, source_parent_id, state)
        if target_id:
            return target_id

    # Parent was seen but not mapped (shouldn't happen) — place at root
    print(f"    [warn] Parent {source_parent_id} seen but unmapped. Placing at root.", file=sys.stderr)
    return None


def process_source_document(
    client: OutlineClient,
    source_doc_id: str,
    state: dict,
) -> str | None:
    """
    Export -> AI-transform -> create in target collection.
    Returns target document ID.
    """
    # Already handled
    if source_doc_id in state["seen_source_ids"]:
        return state["id_mapping"].get(source_doc_id)

    # Cycle guard
    if source_doc_id in _processing_stack:
        print(f"    [!] Cycle detected at {source_doc_id}. Breaking.", file=sys.stderr)
        return None
    _processing_stack.add(source_doc_id)

    try:
        info = get_document_info(client, source_doc_id)
        title = info.get("title", "Untitled")
        source_parent_id = info.get("parentDocumentId")

        print(f"\n=== {title} ({source_doc_id}) ===")

        if DRY_RUN:
            print("    [DRY-RUN] Would export, transform, and create in target.")
            state["seen_source_ids"].append(source_doc_id)
            fake_id = f"dry-run-{source_doc_id}"
            state["id_mapping"][source_doc_id] = fake_id
            save_state(state)
            return fake_id

        # 1. Export
        print("    [1/3] Exporting...")
        raw_md = get_document_text(client, source_doc_id)
        print(f"        -> {len(raw_md)} chars")

        # 2. AI Transform
        print("    [2/3] AI transforming...")
        processed_md = transform_document(title, raw_md)
        print(f"        -> {len(processed_md)} chars")

        # 3. Resolve parent chain in target
        print("    [3/3] Resolving parent in target...")
        target_parent_id = resolve_target_parent(client, source_parent_id, state)

        # 4. Create in target collection
        payload = {
            "title": f"{TITLE_PREFIX}{title}",
            "text": processed_md,
            "collectionId": TARGET_COLLECTION_ID,
            "publish": True,
        }
        if target_parent_id:
            payload["parentDocumentId"] = target_parent_id

        resp = client.post("documents.create", payload)
        target_id = resp.get("data", {}).get("id")
        target_url = resp.get("data", {}).get("url", "N/A")
        print(f"        -> Created: {target_url} (id: {target_id})")

        # 5. Record
        state["seen_source_ids"].append(source_doc_id)
        state["id_mapping"][source_doc_id] = target_id
        save_state(state)

        return target_id

    except Exception as e:
        print(f"    [ERROR] {e}", file=sys.stderr)
        return None
    finally:
        _processing_stack.discard(source_doc_id)


# ----------------------------- MAIN -----------------------------"

def main() -> int:
    if not API_TOKEN or not TARGET_COLLECTION_ID or not SOURCE_COLLECTION_IDS:
        print("ERROR: Set OUTLINE_API_TOKEN, SOURCE_COLLECTION_IDS, TARGET_COLLECTION_ID", file=sys.stderr)
        return 1

    client = OutlineClient(API_TOKEN, BASE_URL)
    state = load_state()

    print(f"[*] Sync starting")
    print(f"    Source(s) : {SOURCE_COLLECTION_IDS}")
    print(f"    Target    : {TARGET_COLLECTION_ID}")
    print(f"    State     : {STATE_FILE.resolve()}")
    print(f"    Seen      : {len(state['seen_source_ids'])} docs")
    print(f"    Mapped    : {len(state['id_mapping'])} docs")
    print(f"    Dry-run   : {DRY_RUN}")
    print("-" * 60)

    # Gather all source documents
    all_source = {}
    for col_id in SOURCE_COLLECTION_IDS:
        all_source.update(fetch_all_docs(client, col_id))

    # Determine truly new documents
    new_ids = [sid for sid in all_source if sid not in state["seen_source_ids"]]

    if not new_ids:
        print("[*] No new documents found. Nothing to do.")
        return 0

    print(f"[+] Found {len(new_ids)} new document(s) to process\n")

    success = 0
    failed = 0
    for sid in new_ids:
        result = process_source_document(client, sid, state)
        if result:
            success += 1
        else:
            failed += 1

    print(f"\n{'='*60}")
    print(f"[*] Done.")
    print(f"    Created : {success}")
    print(f"    Failed  : {failed}")
    print(f"    Skipped : {len(all_source) - len(new_ids)} (already in state)")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n[*] Aborted.")
        sys.exit(130)