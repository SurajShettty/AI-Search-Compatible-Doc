# AI Search Documentation Converter

Convert raw Markdown documentation into AI-search-optimized structured JSON and enhanced Markdown files using the local Claude CLI — without needing any API key.

---

## Features

* Converts `.md` documentation into:

  * Structured JSON for RAG/chatbot systems
  * Cleaned, searchable Markdown
* Uses local `claude` CLI authentication
* No API keys required
* Automatically cleans mojibake/encoding issues
* Generates:

  * Feature summaries
  * Search keywords
  * User questions
  * Synonyms
  * Related features
* Parallel processing with configurable workers
* Retry handling and timeout support

---

# Requirements

## Python

Python 3.10+ recommended.

## Claude CLI

Install Claude Code CLI globally:

```bash
npm install -g @anthropic-ai/claude-code
```

Authenticate once:

```bash
claude
```

---

# Usage

```bash
python doc_to_ai_search.py
```

---

# Configuration

```python
INPUT_PATH = r"c:\path\to\your\markdown_docs"
OUTPUT_DIR = r"c:\path\to\output_folder"
MODULE_HINT = None
```

Optional tuning:

```python
CLAUDE_MODEL = "sonnet"
CLI_TIMEOUT_SEC = 600
MAX_RETRIES = 2
MAX_WORKERS = 4
```

---

# Output

The script generates:

* Structured JSON files for RAG systems
* AI-search-optimized Markdown files
* Feature-level searchable chunks
* Conversational user queries and keywords

---

# Workflow

```text
Raw Markdown
    ↓
Encoding Cleanup
    ↓
Claude CLI Processing
    ↓
Structured JSON
    ↓
AI-Optimized Markdown
```

---

# License

Internal/private usage recommended unless adapted for public release.
