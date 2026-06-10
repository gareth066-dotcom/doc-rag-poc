import re
from pathlib import Path

CHUNK_SIZE = 4000
CHUNK_OVERLAP = 500
TOP_K = 10
MAX_CONTEXT_CHARS = 80_000


def chunk_text(text: str, chunk_size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start = end - overlap

    return chunks


def _query_terms(query: str) -> set[str]:
    return {
        word.lower()
        for word in re.findall(r"\w+", query)
        if len(word) > 2
    }


def retrieve_relevant_chunks(chunks: list[str], query: str, top_k: int = TOP_K) -> list[str]:
    terms = _query_terms(query)

    if not terms:
        return chunks[:top_k]

    scored = []

    for index, chunk in enumerate(chunks):
        chunk_lower = chunk.lower()
        score = sum(1 for term in terms if term in chunk_lower)

        if score:
            scored.append((score, index, chunk))

    if not scored:
        return chunks[:top_k]

    scored.sort(key=lambda item: (-item[0], item[1]))

    selected = []
    total_chars = 0

    for _, _, chunk in scored:
        if total_chars + len(chunk) > MAX_CONTEXT_CHARS:
            break

        selected.append(chunk)
        total_chars += len(chunk)

        if len(selected) >= top_k:
            break

    return selected


def load_relevant_context(content_path: Path, query: str) -> str:
    text = content_path.read_text(encoding="utf-8")
    chunks = chunk_text(text)
    relevant = retrieve_relevant_chunks(chunks, query)
    return "\n\n---\n\n".join(relevant)
