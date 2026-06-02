#!/usr/bin/env python3
"""
init_state_hybrid.py
--------------------
Seed outline_sync_state.json by auto-matching PARENTS (titles match).
For CHILDREN with mismatched titles, auto-guesses when safe (only child)
and prints a manual mapping table for the rest.

Env vars:
  OUTLINE_API_TOKEN
  OUTLINE_BASE_URL        default: https://app.getoutline.com/api
  SOURCE_COLLECTION_IDS   comma-separated
  TARGET_COLLECTION_ID
  TITLE_PREFIX            default: [AI]
  STATE_FILE              default: outline_sync_state.json
"""

import json
from dotenv import load_dotenv
import os
import sys

import requests
load_dotenv() 

TOKEN = os.getenv("OUTLINE_API_TOKEN", "")
BASE_URL = os.getenv("OUTLINE_BASE_URL", "https://app.getoutline.com/api").rstrip("/")
# NOTE: Outline's API requires full collection UUIDs, not the short URL IDs
# shown in the browser (e.g. "TfgiqQsTzQ"). Use collections.list to find them.
SOURCE_COLLECTION_IDS = [c.strip() for c in os.getenv("SOURCE_COLLECTION_IDS", "").split(",") if c.strip()]
TARGET_COLLECTION_ID = os.getenv("TARGET_COLLECTION_ID", "")
TITLE_PREFIX = os.getenv("TITLE_PREFIX", "[AI] ").strip()
STATE_FILE = os.getenv("STATE_FILE", "outline_sync_state.json")


def api_post(endpoint, payload):
    url = f"{BASE_URL}/{endpoint}"
    resp = requests.post(url, json=payload, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    })
    if not resp.ok:
        # Surface Outline's actual validation message instead of a bare status code.
        raise requests.HTTPError(f"{resp.status_code} on {endpoint}: {resp.text}", response=resp)
    return resp.json()


def list_all_docs(collection_id):
    docs = {}
    offset = 0
    while True:
        resp = api_post("documents.list", {
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


def strip_prefix(title):
    if title.startswith(TITLE_PREFIX):
        return title[len(TITLE_PREFIX):].strip()
    return title.strip()


def main():
    if not TOKEN or not TARGET_COLLECTION_ID or not SOURCE_COLLECTION_IDS:
        print("ERROR: Set OUTLINE_API_TOKEN, SOURCE_COLLECTION_IDS, TARGET_COLLECTION_ID", file=sys.stderr)
        sys.exit(1)

    print("[*] Fetching source documents...")
    source_docs = {}
    for col_id in SOURCE_COLLECTION_IDS:
        source_docs.update(list_all_docs(col_id))
    print(f"    Found {len(source_docs)} source doc(s)")

    print("[*] Fetching target documents...")
    target_docs = list_all_docs(TARGET_COLLECTION_ID)
    print(f"    Found {len(target_docs)} target doc(s)")

    # Build lookups
    source_by_title = {}
    for sid, d in source_docs.items():
        t = d.get("title", "").strip()
        if t:
            source_by_title.setdefault(t, []).append(sid)

    source_children = {}  # parent_id -> [child_ids]
    for sid, d in source_docs.items():
        pid = d.get("parentDocumentId")
        if pid:
            source_children.setdefault(pid, []).append(sid)

    # First pass: match by title
    mapping = {}  # source_id -> target_id
    unmatched_target = []

    for tid, d in target_docs.items():
        clean = strip_prefix(d.get("title", ""))
        candidates = source_by_title.get(clean, [])
        if len(candidates) == 1:
            mapping[candidates[0]] = tid
        else:
            unmatched_target.append({
                "target_id": tid,
                "target_title": d.get("title", ""),
                "clean_title": clean,
                "target_parent_id": d.get("parentDocumentId"),
                "reason": f"AMBIGUOUS ({len(candidates)} matches)" if len(candidates) > 1 else "NO MATCH",
            })

    title_matched = len(mapping)
    print(f"    Title-matched: {title_matched}")

    # Second pass: analyze unmatched by parent structure
    auto_guesses = []
    manual_needed = []

    # Reverse mapping for quick parent lookup
    target_to_source = {v: k for k, v in mapping.items()}

    for u in unmatched_target:
        t_parent = u["target_parent_id"]
        source_parent_id = target_to_source.get(t_parent)

        if source_parent_id:
            children = source_children.get(source_parent_id, [])
            parent_title = source_docs.get(source_parent_id, {}).get("title", "???")

            if len(children) == 1:
                # Only one source child — safe guess
                cid = children[0]
                mapping[cid] = u["target_id"]
                auto_guesses.append({
                    "source_id": cid,
                    "source_title": source_docs[cid]["title"],
                    "target_id": u["target_id"],
                    "target_title": u["target_title"],
                    "parent": parent_title,
                })
            else:
                manual_needed.append({
                    "target_id": u["target_id"],
                    "target_title": u["target_title"],
                    "parent_title": parent_title,
                    "parent_source_id": source_parent_id,
                    "candidates": [
                        {"id": cid, "title": source_docs[cid]["title"]}
                        for cid in children
                    ],
                })
        else:
            manual_needed.append({
                "target_id": u["target_id"],
                "target_title": u["target_title"],
                "parent_title": "(unmapped or root)",
                "parent_source_id": None,
                "candidates": [],
            })

    # Write state
    state = {
        "seen_source_ids": list(mapping.keys()),
        "id_mapping": mapping,
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    # Report
    print(f"\n{'='*60}")
    print(f"[*] STATE WRITTEN: {STATE_FILE}")
    print(f"    Title-matched parents : {title_matched}")
    print(f"    Auto-guessed children : {len(auto_guesses)}")
    print(f"    Manual map needed     : {len(manual_needed)}")

    if auto_guesses:
        print(f"\n[+] AUTO-GUESSED (review & confirm):")
        for g in auto_guesses:
            print(f"    '{g['source_title']}'  ->  '{g['target_title']}'  (under: {g['parent']})")

    if manual_needed:
        print(f"\n[!] MANUAL MAPPING NEEDED — copy the correct lines below into {STATE_FILE}:")
        print(f"    Under the \"id_mapping\" object, add:")
        for m in manual_needed:
            print(f"\n    # Target: '{m['target_title']}'  (parent: {m['parent_title']})")
            if m["candidates"]:
                for c in m["candidates"]:
                    print(f'    "{c["id"]}": "{m["target_id"]}",  # {c["title"]}')
            else:
                print(f'    # No candidates. Find the source doc manually.')
                print(f'    "SOURCE-UUID-HERE": "{m["target_id"]}",')

    unmatched_source = [sid for sid in source_docs if sid not in mapping]
    if unmatched_source:
        print(f"\n[*] {len(unmatched_source)} source doc(s) will be treated as NEW on next run:")
        for sid in unmatched_source[:10]:
            print(f"    - '{source_docs[sid]['title']}' ({sid})")
        if len(unmatched_source) > 10:
            print(f"    ... and {len(unmatched_source) - 10} more")

    print(f"\n[*] After editing {STATE_FILE}, run: python outline_sync_new.py")


if __name__ == "__main__":
    main()