# Cost Analysis — Doc-to-AI-Search Pipeline

Detailed per-document and 100-document cost estimates for the documentation
conversion pipeline, plus a side-by-side comparison of the CLI (no-key) and
API-key script variants.

Pricing assumes **Claude Sonnet 4.6** at the published rates:
`$3 / million input tokens`, `$15 / million output tokens`,
`$3.75 / million cache-write tokens`, `$0.30 / million cache-read tokens`.

## Token estimates

Rule of thumb: **~4 characters per token** for English Markdown.

| Doc size      | Input tokens (doc only) |
| ------------- | ----------------------- |
| Average (4-5 KB)   | ~1,000-1,250           |
| Max (10-15 KB)     | ~2,500-3,750           |

Plus fixed overhead per call:

- **System prompt:** ~600 tokens
- **Wrapper text** (filename, module hint, BEGIN/END markers): ~50 tokens

Output is harder to predict — the schema asks for 15-25 keywords and 5-12
user questions *per chunk*, and a 5 KB doc typically produces 3-6 chunks.
Expect **output ≈ 2-3× input** in tokens.

## Per-document cost

### Average document (~5 KB)

| Item                       | Tokens   | Cost      |
| -------------------------- | -------- | --------- |
| System prompt (input)      | 600      | $0.0018   |
| Document + wrapper (input) | 1,200    | $0.0036   |
| Structured JSON (output)   | ~3,500   | $0.0525   |
| **Per doc**                |          | **~$0.058** |

### Max-size document (~15 KB)

| Item                       | Tokens   | Cost      |
| -------------------------- | -------- | --------- |
| System prompt (input)      | 600      | $0.0018   |
| Document + wrapper (input) | 3,200    | $0.0096   |
| Structured JSON (output)   | ~6,000   | $0.090    |
| **Per doc**                |          | **~$0.101** |

## 100-document totals

| Scenario                                   | No caching | With caching |
| ------------------------------------------ | ---------- | ------------ |
| All average (~5 KB)                        | ~$5.80     | ~$5.65       |
| Realistic mix (mostly 5 KB, a few 15 KB)   | ~$6-7      | ~$6-7        |
| All max-size (~15 KB)                      | ~$10.10    | ~$9.95       |

**Note on caching:** Prompt caching saves only ~$0.15-0.20 across 100 docs.
The system prompt is small relative to per-doc input, and output tokens
(which dominate the bill) are not cacheable.

## Pros / cons by script

### `doc_to_ai_search_without_key.py` — CLI / no API key

| Pros                                            | Cons                                                |
| ----------------------------------------------- | --------------------------------------------------- |
| $0 marginal cost (uses your Claude subscription) | Per-call Node.js + auth overhead → slower wall time |
| No API key to manage or leak                    | Subject to subscription rate-limit pauses           |
| Same model, same output quality                 | No prompt-caching benefit                           |
| Already parallelised (`MAX_WORKERS`)            | Subprocess plumbing makes debugging messier         |

### `doc_to_ai_search.py` — API key

| Pros                                                       | Cons                                          |
| ---------------------------------------------------------- | --------------------------------------------- |
| Faster per call (no subprocess; caching helps a little)    | Costs ~$6 per 100 docs                        |
| Predictable rate-limit headroom (separate from subscription) | Requires `ANTHROPIC_API_KEY`                  |
| Cleaner errors / retries via SDK                           | Bill scales linearly with volume              |

## Bottom line

For batches up to a few hundred docs, the **CLI version is the better
choice** — zero marginal cost, same output. Switch to the **API version**
only if you hit subscription rate-limit pauses, need predictable throughput,
or plan to run thousands of documents.

## Caveats

- Token counts are estimates; actuals depend on the specific document
  content and how many chunks the model produces.
- Output cost dominates total cost (output tokens are 5× the price of input).
- Sonnet 4.6 pricing may change; verify current rates before budgeting.
