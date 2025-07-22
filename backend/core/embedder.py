from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from backend.config import EMBED_MODEL, CHROMA_DB_PATH

def embed_and_store(chunks: list[str], document_id: str = "default_doc") -> Chroma:
    # Create embedding model
    embed_model = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    # Add metadata for traceability (can expand later)
    metadatas = [{"source": document_id, "chunk_index": i} for i in range(len(chunks))]

    # Create or load ChromaDB and add embeddings
    vectordb = Chroma.from_texts(texts=chunks, embedding=embed_model, metadatas=metadatas, persist_directory=CHROMA_DB_PATH)
    vectordb.persist()
    return vectordb
