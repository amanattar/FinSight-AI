from langchain.chains import RetrievalQA
from backend.core.retriever import get_retriever
from backend.core.generator import get_llm

def get_rag_chain():
    retriever = get_retriever()
    llm = get_llm()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
