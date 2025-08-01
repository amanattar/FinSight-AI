import os
from dotenv import load_dotenv

load_dotenv()

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./data/uploads")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./backend/vector_store/chroma_db")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 5))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 1))
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "./backend/vector_store/chroma_db")
LLM_MODEL = os.getenv("LLM_MODEL", "mistral")
COLLECTION_NAME = "finsight_chunks"

