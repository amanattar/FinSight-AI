import os
import streamlit as st
from dotenv import load_dotenv
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.file_loader import load_financial_data, normalize_table
from backend.core.chunker import chunk_rows
from backend.core.embedder import embed_and_store
from backend.core.rag_pipeline import get_rag_chain
from backend.config import COLLECTION_NAME

# Load environment variables
load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./data/uploads")

st.set_page_config(page_title="FinSight AI")
st.title("📄 FinSight AI – Financial Document Analyzer")

# File uploader for structured data
uploaded_file = st.file_uploader("📤 Upload financial document", type=["csv", "xlsx", "xls", "json"])

if uploaded_file:
    # Save file to uploads directory
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

    try:
        # Load structured data as DataFrame
        df = load_financial_data(uploaded_file)
        st.subheader("📊 Data Preview")
        st.dataframe(df.head(20))

        # Normalize into plain text rows
        full_text = normalize_table(df)

        # Step 3: Chunk the data
        chunks = chunk_rows(full_text)
        st.write(f"🧩 Created {len(chunks)} text chunks.")
        st.subheader("🧩 Chunk Preview")
        for i, chunk in enumerate(chunks):
            st.text_area(f"Chunk {i+1}", chunk, height=150)

        # Step 4: Embed and store chunks
        with st.spinner("🔄 Embedding chunks and storing in ChromaDB..."):
            vectordb = embed_and_store(chunks, uploaded_file.name)
            st.success("✅ Chunks embedded and stored in vector database.")

        # Step 5: Ask a question
        st.subheader("💬 Ask a question about the document")
        user_query = st.text_input("Your question")

        if user_query:
            with st.spinner("🧠 Thinking..."):
                rag_chain = get_rag_chain()
                result = rag_chain(user_query)
                st.markdown("### 🧾 Answer:")
                st.write(result["result"])

                st.markdown("### 📚 Top Source Chunks:")
                for i, doc in enumerate(result["source_documents"]):
                    st.text_area(f"Source {i+1}", doc.page_content, height=150)

    except Exception as e:
        st.error(f"❌ Failed to process file: {e}")
