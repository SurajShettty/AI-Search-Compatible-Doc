# Outline Sync — Complete Flow

This document explains how the two scripts work, end to end.

## Prerequisites

Before running either script, make sure all of the following are in place.

### 1. Software

| Requirement   | Notes                                                                 |
| ------------- | --------------------------------------------------------------------- |
| **Python 3.9+** | The scripts use modern typing (`from __future__ import annotations`). |
| **Claude CLI**  | The `claude` command must be installed and on your `PATH` (or point to it with `CLAUDE_CLI_PATH`). Used by `outline_sync_new.py` for the AI transform. |
| **Python packages** | Install with: `pip install requests python-dotenv`                |

### 2. Outline access

- An **Outline API token** with read access to the source collection(s) and
  read/write access to the target collection.
- The **full collection UUIDs** (not the short URL IDs) for both source and
  target collections.

### 3. `.env` file

Create a `.env` file in the project root. **Required** variables:

```bash
# Outline API token (read source, read/write target)
OUTLINE_API_TOKEN=your-token-here

# Full collection UUIDs (comma-separate multiple sources)
SOURCE_COLLECTION_IDS=046cc88e-b8cc-44cb-a670-75ab40030e6f
TARGET_COLLECTION_ID=83fe623e-b90c-4ae2-9760-873f3162aecc
```

**Optional** variables (defaults shown):

| Variable           | Default                          | Purpose                                      |
| ------------------ | -------------------------------- | -------------------------------------------- |
| `OUTLINE_BASE_URL` | `https://app.getoutline.com/api` | Override for self-hosted Outline instances.  |
| `CLAUDE_CLI_PATH`  | `claude`                         | Explicit path to the Claude CLI binary.      |
| `STATE_FILE`       | `outline_sync_state.json`        | Path to the sync state file.                 |
| `DRY_RUN`          | `false`                          | Set `true` to preview without writing.       |

> ⚠️ The `.env` file holds your API token — keep it out of version control
> (it's already in `.gitignore`).

### 4. First-run order

Run `init_state_hybrid.py` **once** before the first `outline_sync_new.py` run to
seed `outline_sync_state.json` from docs that already exist in both collections.
See the two script sections below for details.

---

## The Big Picture

You have two Outline collections:

- **Source** (`046cc88e-…`) — raw, human-written feature docs (possibly with messy
  encoding, tables, etc.).
- **Target** (`83fe623e-…`) — AI-optimized copies structured for a RAG chatbot
  (rich keywords, synonyms, user questions, etc.).

**Goal:** keep the target collection in sync with the source, mirror the
parent/child tree, and run every doc through Claude to rewrite it into
search-optimized form.

The link between them is **`outline_sync_state.json`**, which holds three maps:

| Key                 | Meaning                                                          |
| ------------------- | ---------------------------------------------------------------- |
| `seen_source_ids`   | Source docs already processed (so they aren't re-created)        |
| `id_mapping`        | `source doc id → target doc id` (so updates hit the right target)|
| `source_updated_at` | `source doc id → last-synced updatedAt` (change-detection baseline)|

---

## Script 1: `init_state_hybrid.py` — One-Time Setup

Run **once**. Its job is to build the initial `outline_sync_state.json` by
matching docs that **already exist** in both collections, so the sync script
doesn't create duplicates of things you've already copied over manually.

### Flow

1. **Fetch both trees** (`list_all_docs`) — pulls every doc (published + draft)
   from the source collection(s) and the target collection via `documents.list`,
   paginating 100 at a time.

2. **Build child indexes** — for each tree, maps `parentDocumentId → [child ids]`
   (with `None` = root level).

3. **Top-down tree alignment by title** — walks both trees from the root. At each
   matched parent pair, it matches children by exact title.
   - Children are matched **only after their parent is matched**, so two docs both
     named "FAQ" under different modules get disambiguated by position in the tree.
   - `core_title` strips an optional `"<parent> - "` prefix before comparing
     (legacy from an older naming scheme), so it works whether titles are bare or
     prefixed.
   - `by_created` sorts siblings by creation date so duplicate-named siblings
     align deterministically.

4. **Write state** — produces:
   - `seen_source_ids` = matched source ids
   - `id_mapping` = source→target for every matched pair
   - `source_updated_at` = each matched source doc's current `updatedAt`
     (the **change-detection baseline**, so updates can be detected on the very
     next sync run)

5. **Report** — prints counts and lists:
   - **Unmatched source docs** → no title match in the target, so they'll be
     created as NEW on the next sync. Rename target docs to match if you want them
     linked instead.
   - **Orphan target docs** → exist in target but match no source; left untouched.

> ⚠️ Re-running this **overwrites** the whole state file, resetting all baselines.
> Only do it for a fresh setup/rebuild — never during normal operation.

---

## Script 2: `outline_sync_new.py` — The Recurring Sync

This is the script you run regularly. It detects new + changed source docs,
transforms them via Claude, and creates/updates them in the target.

### Configuration

Loads env vars from `.env`: API token, source/target collection IDs, base URL,
Claude CLI path, state file path, dry-run flag. Claude runs with
`model = "sonnet"`, a 600s timeout, and 2 retries.

### `main()` — the orchestrator

1. **Load state** (`load_state`) — reads the JSON, defaulting any missing keys to
   empty.

2. **Gather all source docs** — `fetch_all_docs` lists every doc in the source
   collection(s), giving an `id → doc` dict (each doc includes its live
   `updatedAt`).

3. **Find NEW docs** — any source id not in `seen_source_ids`.

4. **Find CHANGED docs** — for each already-seen doc:
   - Compare live `updatedAt` (from `documents.list`) against stored
     `source_updated_at`.
   - If no baseline exists (`None`), **backfill** it without regenerating and set a
     `backfilled` flag (this now gets saved — see "Bugs fixed" below).
   - If live ≠ stored → add to `updated_ids`.
   - Save state if anything was backfilled.

5. **Process NEW docs** → `process_source_document` for each.

6. **Process CHANGED docs** → `update_source_document` for each.

7. **Print summary** — created/updated, failed, unchanged counts.

### `process_source_document` — handles NEW docs

1. Skip if already seen; **cycle guard** via `_processing_stack` to avoid infinite
   recursion on parent loops.
2. Fetch doc info (title, `parentDocumentId`, `updatedAt`) via `documents.info`.
3. **Export** the raw markdown (`get_document_text` → `documents.export`).
4. **AI-transform** (`transform_document`) — see below.
5. **Resolve parent in target** (`resolve_target_parent`):
   - If the source parent is already in `id_mapping`, use the mapped target id.
   - If the parent is unseen, **recursively process the parent first** so the tree
     is built top-down, then nest under it.
   - If a parent is seen but somehow unmapped, place at root with a warning.
6. **Create** in target via `documents.create` (with `parentDocumentId` if there's
   a parent), published.
7. **Record** the source id in `seen_source_ids`, `id_mapping`, and
   `source_updated_at`; save state.

### `update_source_document` — handles CHANGED docs

1. Look up the target id from `id_mapping`. If missing (synced before mapping
   existed), fall back to treating it as new.
2. Fetch info, re-export, re-transform (same steps as create).
3. **Update in place** via `documents.update` (same target id — no new doc, no
   tree re-resolution since the doc already lives where it belongs).
4. Record the new `updatedAt` baseline; save state.

### `transform_document` — the Claude step

1. Locates the `claude` CLI (`_find_claude`).
2. Writes the `SYSTEM_PROMPT` (RAG-transformer instructions: output schema,
   mojibake cleanup, acronym expansion, aggressive keyword/synonym/user-question
   generation) to a temp file.
3. Builds the user message (source filename + the raw markdown).
4. Runs `claude -p --model sonnet --system-prompt-file … --output-format text`,
   piping the doc in via stdin. Retries up to 2× with exponential backoff on
   failure/timeout/bad-JSON.
5. `_extract_json` strips any code fences and pulls out the JSON object Claude
   returns.
6. `render_markdown` turns that JSON (`doc` + `chunks`) into the final structured
   markdown: title, module, tags, overview, prerequisites, then one section per
   chunk (what it does / why it matters / how to use / examples / questions this
   answers / keywords / synonyms / related / tags).

---

## Your Day-to-Day Loop

```bash
# 1. Edit source docs in Outline
# 2. Run the sync
python outline_sync_new.py
```

That's it:

- **New** source docs → transformed and **created** under the right parent.
- **Changed** source docs (edited since last run) → re-transformed and **updated
  in place**.
- **Unchanged** docs → skipped.
- The state file (`source_updated_at`) is updated automatically each run.

Set `DRY_RUN=true` to preview what would happen without writing to Outline.

> Only run `init_state_hybrid.py` for initial setup (or a deliberate full rebuild).
> Running it again resets the baselines.

---

## Change Detection Caveats

Change detection relies on `updatedAt`. Two things to watch:

- An edit that doesn't bump `updatedAt` (or one made **before** a re-seed) won't be
  picked up.
- Re-running `init_state_hybrid.py` after editing a doc bakes that edit into the
  baseline, so it will no longer be seen as "changed".

To verify the pipeline: edit a source doc → run `outline_sync_new.py` → confirm it
reports the doc as changed and updates the target.

---

## Bugs Fixed

1. **`outline_sync_new.py`** — backfilled timestamps were being discarded (state was
   saved only when an update was already found). Now persisted via a `backfilled`
   flag, so the baseline survives and future runs can detect changes.
2. **`init_state_hybrid.py`** — wasn't seeding `source_updated_at` at all, so there
   was never a baseline. Now it records each matched source doc's `updatedAt` at
   seed time.
