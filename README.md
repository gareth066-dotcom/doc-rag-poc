# doc-rag-poc

A small proof of concept for asking questions about a document using OpenAI.

1. Extract text from a PDF into a plain-text file.
2. Send the full document plus your question to GPT and print the answer.

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

Place your PDF at `data/sample.pdf` (or update the path in `src/extract.py`).

## Usage

Run commands from the project root.

**1. Extract text from the PDF**

```bash
python3 src/extract.py
```

This writes `extracted/content.txt`.

**2. Ask a question**

```bash
python3 src/ask.py
```

Enter your question when prompted. The script sends the extracted document and your question to GPT and prints the response.

## Project layout

```
data/           Source documents (e.g. sample.pdf)
extracted/      Generated text output (gitignored)
src/
  extract.py    PDF → plain text
  ask.py        Question answering via OpenAI
```

## Notes

- On macOS, use `python3` if `python` is not available.
- `extracted/` and `.env` are gitignored. Do not commit API keys.
- This POC sends the entire document in each request. It does not use chunking or vector search yet.
