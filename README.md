# AI Search Documentation Converter & Outline Sync

Keep two Outline collections in sync: take raw, human-written docs from a **Source**
collection, run each one through Claude AI to rewrite it into a search-optimized
(chatbot/RAG-friendly) format, and publish the result into a **Target** collection —
mirroring the same parent/child tree.

Uses the local **Claude CLI** for the AI transform — **no API key required**.

> For the full end-to-end walkthrough, see [SYNC_FLOW.md](SYNC_FLOW.md).

---

## How It Works

You have two Outline collections:

* **Source** → raw, human-written feature docs (possibly with messy encoding, tables, etc.).
* **Target** → AI-optimized copies structured for a RAG chatbot (keywords, synonyms, user questions, etc.).

The sync mirrors the source tree into the target and runs every doc through Claude to
rewrite it into search-optimized form. The link between them is `outline_sync_state.json`,
which tracks what's already synced, source→target id mappings, and last-synced timestamps
(for change detection).

---

## Features

* Syncs raw Outline docs into AI-search-optimized docs in a target collection
* Mirrors the parent/child document tree
* Uses local `claude` CLI authentication — **no API keys required**
* Detects **new** and **changed** source docs automatically (via `updatedAt`)
* Automatically cleans mojibake/encoding issues
* Generates feature summaries, search keywords, user questions, synonyms, related features
* Retry handling and timeout support
* `DRY_RUN` mode to preview changes without writing

---

## The Two Scripts

| Script | When to run | Purpose |
| ------ | ----------- | ------- |
| `init_state_hybrid.py` | **Once** (initial setup) | Matches docs that already exist in *both* collections (by title + tree position) and seeds `outline_sync_state.json` so the sync doesn't create duplicates. |
| `outline_sync_new.py`  | **Regularly** (day-to-day) | Detects new + changed source docs, transforms them via Claude, and creates/updates them in the target. |

> ⚠️ Re-running `init_state_hybrid.py` **overwrites** the whole state file and resets all
> change-detection baselines. Only do it for a fresh setup or a deliberate full rebuild.

---

## Requirements

### Python

Python 3.9+ (the scripts use modern typing).

### Claude CLI

Install Claude Code CLI globally:

```bash
npm install -g @anthropic-ai/claude-code
```

Authenticate once:

```bash
claude
```

### Python packages

```bash
pip install requests python-dotenv
```

### Outline access

* An **Outline API token** with read access to the source collection(s) and read/write access to the target collection.
* The **full collection UUIDs** (not the short URL IDs) for both source and target collections.

---

## Configuration

Create a `.env` file in the project root.

**Required:**

```bash
# Outline API token (read source, read/write target)
OUTLINE_API_TOKEN=your-token-here

# Full collection UUIDs (comma-separate multiple sources)
SOURCE_COLLECTION_IDS=046cc88e-b8cc-44cb-a670-75ab40030e6f
TARGET_COLLECTION_ID=83fe623e-b90c-4ae2-9760-873f3162aecc
```

**Optional** (defaults shown):

| Variable           | Default                          | Purpose                                     |
| ------------------ | -------------------------------- | ------------------------------------------- |
| `OUTLINE_BASE_URL` | `https://app.getoutline.com/api` | Override for self-hosted Outline instances. |
| `CLAUDE_CLI_PATH`  | `claude`                         | Explicit path to the Claude CLI binary.     |
| `STATE_FILE`       | `outline_sync_state.json`        | Path to the sync state file.                |
| `DRY_RUN`          | `false`                          | Set `true` to preview without writing.      |

> ⚠️ The `.env` file holds your API token — keep it out of version control (it's already in `.gitignore`).

---

## Usage

**First-time setup** (run once):

```bash
python init_state_hybrid.py
```

**Day-to-day loop:**

```bash
# 1. Edit source docs in Outline
# 2. Run the sync
python outline_sync_new.py
```

That's it:

* **New** source docs → transformed and **created** under the right parent.
* **Changed** source docs (edited since last run) → re-transformed and **updated in place**.
* **Unchanged** docs → skipped.
* The state file is updated automatically each run.

Set `DRY_RUN=true` to preview what would happen without writing to Outline.

---

## Workflow

```text
Source Outline collection (raw docs)
    ↓
Export raw Markdown
    ↓
Encoding cleanup
    ↓
Claude CLI processing (RAG transform)
    ↓
Structured JSON → AI-optimized Markdown
    ↓
Create / update in Target Outline collection (tree mirrored)
```

---

## Change Detection Caveats

Change detection relies on the `updatedAt` field:

* An edit that doesn't bump `updatedAt` (or one made **before** a re-seed) won't be picked up.
* Re-running `init_state_hybrid.py` after editing a doc bakes that edit into the baseline, so it will no longer be seen as "changed".

To verify the pipeline: edit a source doc → run `outline_sync_new.py` → confirm it reports the doc as changed and updates the target.

---

## Automation Note

We tried to automate this for near-instant updates using **GitHub Actions**, but it required
an `ANTHROPIC_API_KEY`. This wasn't possible with our current setup, which uses the
**Claude CLI** (not the API key) for the AI transform.

---

## License

Internal/private usage recommended unless adapted for public release.
