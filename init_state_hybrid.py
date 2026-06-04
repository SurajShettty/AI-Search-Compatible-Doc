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

    # Build child indexes for both trees (parent_id -> [doc_ids]; None = root).
    source_children = {}
    for sid, d in source_docs.items():
        source_children.setdefault(d.get("parentDocumentId"), []).append(sid)
    target_children = {}
    for tid, d in target_docs.items():
        target_children.setdefault(d.get("parentDocumentId"), []).append(tid)

    def core_title(target_title, source_parent_title):
        """Target titles may carry a '<parent> - ' prefix added by outline_sync.
        Strip it so we compare against the source doc's bare title."""
        t = (target_title or "").strip()
        if source_parent_title:
            prefix = f"{source_parent_title} - "
            if t.startswith(prefix):
                return t[len(prefix):].strip()
        return t

    def by_created(docs, ids):
        # Stable order so duplicate-named siblings align deterministically.
        return sorted(ids, key=lambda i: docs[i].get("createdAt", ""))

    # Top-down tree alignment by exact name. A level's children are matched only
    # after their parent is matched, so identical names under different parents
    # (e.g. each module's 'FAQs') are disambiguated by position. An optional
    # '<parent> - ' prefix is stripped from both sides, so it works whether titles
    # are bare or 'parent - child'. (Assumes target titles match the source after
    # the manual rename; anything still unmatched is reported below.)
    mapping = {}                # source_id -> target_id
    matched_targets = set()

    queue = [(None, None)]      # (matched source parent, matched target parent); roots first
    while queue:
        s_par, t_par = queue.pop()
        s_par_title = source_docs.get(s_par, {}).get("title", "").strip() if s_par else ""
        s_kids = by_created(source_docs, source_children.get(s_par, []))
        t_kids = by_created(target_docs, target_children.get(t_par, []))

        for sid in s_kids:
            s_core = core_title(source_docs[sid].get("title", "").strip(), s_par_title)
            found = None
            for tid in t_kids:
                if tid in matched_targets:
                    continue
                if core_title(target_docs[tid].get("title", ""), s_par_title) == s_core:
                    found = tid
                    break
            if found is not None:
                mapping[sid] = found
                matched_targets.add(found)
                queue.append((sid, found))     # descend into the matched pair

    matched_n = len(mapping)
    orphan_targets = [d for tid, d in target_docs.items() if tid not in matched_targets]
    unmatched_source = [sid for sid in source_docs if sid not in mapping]

    # Write state. Seed source_updated_at from the live updatedAt of each matched
    # source doc so outline_sync_new.py has a baseline immediately and can detect
    # changes on the very next run (instead of spending a run just to backfill).
    state = {
        "seen_source_ids": list(mapping.keys()),
        "id_mapping": mapping,
        "source_updated_at": {
            sid: source_docs[sid].get("updatedAt", "") for sid in mapping
        },
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

    # Report
    print(f"\n{'='*60}")
    print(f"[*] STATE WRITTEN: {STATE_FILE}")
    print(f"    Matched docs           : {matched_n}")
    print(f"    Source unmatched (NEW) : {len(unmatched_source)}")
    print(f"    Orphan target docs     : {len(orphan_targets)}")

    if unmatched_source:
        print(f"\n[!] {len(unmatched_source)} source doc(s) have NO matching target title.")
        print(f"    Rename the target doc to match (or they'll be created as NEW on sync):")
        for sid in unmatched_source[:30]:
            d = source_docs[sid]
            par = source_docs.get(d.get("parentDocumentId"), {}).get("title", "(root)")
            print(f"    - '{d['title']}'  (under: {par})")
        if len(unmatched_source) > 30:
            print(f"    ... and {len(unmatched_source) - 30} more")

    if orphan_targets:
        print(f"\n[*] {len(orphan_targets)} target doc(s) matched no source (extra in target, left alone).")

    print(f"\n[*] Goal: rename target docs until 'unmatched' reaches 0, then run:")
    print(f"    python outline_sync_new.py")


if __name__ == "__main__":
    main()