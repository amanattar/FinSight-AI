from langchain_community.llms import Ollama
from backend.config import LLM_MODEL

def get_llm():
    return Ollama(model=LLM_MODEL)
