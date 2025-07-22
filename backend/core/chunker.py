from langchain.text_splitter import RecursiveCharacterTextSplitter
from backend.config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_rows(row_text: str, chunk_size: int = 10, chunk_overlap: int = 2) -> list[str]:
    rows = row_text.strip().split("\n")
    chunks = []
    i = 0
    while i < len(rows):
        chunk = "\n".join(rows[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - chunk_overlap
    return chunks
