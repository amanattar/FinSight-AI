from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.config import CHROMA_DB_PATH, EMBED_MODEL

def get_retriever():
    embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vectordb = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embedder)
    return vectordb.as_retriever(search_kwargs={"k": 15})
