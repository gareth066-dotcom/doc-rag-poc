# doc-rag-poc

A small proof of concept for asking questions about documents using OpenAI.

1. Ingest files from `data/` (PDF, DOCX, PPTX, CSV, XLSX) into a single text file.
2. Retrieve relevant excerpts from that text for each question.
3. Send only those excerpts plus your question to GPT and print the answer.

## Requirements

- Python 3.11+
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
OPENAI_API_KEY=sk-your-key-here
```

Add your documents to `data/`. Supported formats: `.pdf`, `.docx`, `.pptx`, `.csv`, `.xlsx`.

## Usage

Run commands from the project root.

**1. Ingest documents**

```bash
python3 src/ingest.py
```

This processes every file in `data/` and writes `extracted/content.txt`.

**2. Ask a question**

```bash
python3 src/ask.py
```

Enter your question when prompted. Type `exit` to quit.

The script retrieves the most relevant chunks from the ingested text, then sends those excerpts to GPT. This keeps requests within the model context window for large documents.

## Project layout

```
data/                    Source documents
extracted/               Generated text output (gitignored)
src/
  ingest.py              Multi-format document ingestion
  extractor_factory.py   Picks the right extractor by file type
  extractors/            PDF, DOCX, PPTX, CSV, XLSX extractors
  retrieve.py            Chunking and keyword-based retrieval
  ask.py                 Question answering via OpenAI
```

## Notes

- On macOS, use `python3` if `python` is not available.
- `extracted/` and `.env` are gitignored. Do not commit API keys.
- Retrieval is keyword-based, not embeddings. It works well for specific names or terms, but may miss paraphrased questions.
