"""
doc_to_ai_search.py
-------------------
Convert Digii product documentation (Markdown) into AI-search-compatible
structured JSON + a cleaned, keyword-rich Markdown version for use by a
RAG chatbot.

Pipeline:
    .md (raw)  ->  Claude (Sonnet 4.6, with prompt caching)  ->  structured JSON
                                                              ->  rendered Markdown

Usage:
    Edit INPUT_PATH / OUTPUT_DIR / MODULE_HINT below, then:
        python doc_to_ai_search.py

Requires:
    pip install anthropic
    set ANTHROPIC_API_KEY=sk-ant-...
"""

from __future__ import annotations

import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

from anthropic import Anthropic, APIError

# ----------------------------- config (edit here) -----------------------------

INPUT_PATH = r"c:\Users\suraj\Downloads\My Python\Digii Other\Documentations"
OUTPUT_DIR = r"c:\Users\suraj\Downloads\My Python\Digii Other\ai_docs_out"
MODULE_HINT: str | None = None

MODEL = "claude-sonnet-4-6"
MAX_OUTPUT_TOKENS = 8192
MAX_RETRIES = 2

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
   - 'â' or 'â' followed by garbage -> em dash '—'
   - 'â' -> '’' apostrophe
   - 'â' / 'â' -> curly quotes
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


# ----------------------------- text cleanup -----------------------------

_MOJIBAKE = {
    "â": "—",
    "â": "–",
    "â": "’",
    "â": "‘",
    "â": "“",
    "â": "”",
    "â¦": "…",
    "Â ": " ",
    "Â": "",
}


def clean_text(s: str) -> str:
    for bad, good in _MOJIBAKE.items():
        s = s.replace(bad, good)
    return s


# ----------------------------- LLM call -----------------------------

def transform_with_claude(client: Anthropic, source_text: str, source_name: str, module_hint: str | None) -> dict[str, Any]:
    user_msg = (
        f"Source filename: {source_name}\n"
        f"Module hint (may be empty): {module_hint or ''}\n\n"
        f"--- BEGIN DOCUMENT ---\n{source_text}\n--- END DOCUMENT ---"
    )

    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = client.messages.create(
                model=MODEL,
                max_tokens=MAX_OUTPUT_TOKENS,
                system=[
                    {
                        "type": "text",
                        "text": SYSTEM_PROMPT,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[{"role": "user", "content": user_msg}],
            )
            raw = "".join(block.text for block in resp.content if block.type == "text").strip()
            return _extract_json(raw)
        except (APIError, json.JSONDecodeError) as e:
            last_err = e
            wait = 2 ** attempt
            print(f"  ! attempt {attempt} failed ({e.__class__.__name__}); retry in {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"Claude transform failed after {MAX_RETRIES} attempts: {last_err}")


def _extract_json(raw: str) -> dict[str, Any]:
    # Strip code fences if the model added them despite instructions
    fence = re.match(r"^```(?:json)?\s*(.*?)\s*```$", raw, re.DOTALL)
    if fence:
        raw = fence.group(1)
    # Find the outermost {...}
    start = raw.find("{")
    end = raw.rfind("}")
    if start == -1 or end == -1:
        raise json.JSONDecodeError("no JSON object found", raw, 0)
    return json.loads(raw[start : end + 1])


# ----------------------------- markdown renderer -----------------------------

def render_markdown(data: dict[str, Any]) -> str:
    doc = data.get("doc", {})
    chunks = data.get("chunks", [])

    out: list[str] = []
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


# ----------------------------- IO -----------------------------

def gather_inputs(input_path: Path) -> list[Path]:
    if input_path.is_file():
        return [input_path]
    if input_path.is_dir():
        return sorted(input_path.rglob("*.md"))
    raise FileNotFoundError(input_path)


def process_one(src: Path, out_dir: Path, client: Anthropic, module_hint: str | None) -> None:
    print(f"-> {src.name}")
    raw = clean_text(src.read_text(encoding="utf-8", errors="replace"))
    data = transform_with_claude(client, raw, src.name, module_hint)

    base = src.stem.replace(" ", "_")
    json_path = out_dir / f"{base}.json"
    md_path = out_dir / f"{base}.md"

    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(render_markdown(data), encoding="utf-8")
    n_chunks = len(data.get("chunks", []))
    print(f"   wrote {json_path.name} + {md_path.name}  ({n_chunks} chunks)")


def main() -> int:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: set ANTHROPIC_API_KEY first.", file=sys.stderr)
        return 1

    in_path = Path(INPUT_PATH)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)

    client = Anthropic()
    files = gather_inputs(in_path)
    if not files:
        print(f"No .md files found under {in_path}", file=sys.stderr)
        return 1

    print(f"Converting {len(files)} file(s) -> {out_dir}")
    for f in files:
        try:
            process_one(f, out_dir, client, MODULE_HINT)
        except Exception as e:
            print(f"   FAILED: {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
