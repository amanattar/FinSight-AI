import os
import streamlit as st
from dotenv import load_dotenv
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.core.pdf_parser import extract_text_from_pdf
from backend.core.chunker import chunk_text
from backend.core.embedder import embed_and_store

# Load environment variables
load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./data/uploads")

st.set_page_config(page_title="FinSight AI")
st.title("📄 FinSight AI – Financial Document Analyzer")

# File uploader
uploaded_file = st.file_uploader("Upload a financial document (PDF only)", type=["pdf"])

if uploaded_file:
    # Save file to uploads directory
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")

    # Extract text from the saved PDF
    full_text, page_count = extract_text_from_pdf(save_path, uploaded_file.name)
    
    # Show sample preview
    if full_text:

        st.write(f"📄 Extracted from {page_count} pages.")

        # Step 3: Chunk the extracted text
        chunks = chunk_text(full_text)
        st.write(f"🧩 Created {len(chunks)} text chunks.")


        with st.spinner("🔄 Embedding chunks and storing in ChromaDB..."):
            vectordb = embed_and_store(chunks, uploaded_file.name)
            st.success("✅ Chunks embedded and stored in vector database.")

        st.subheader("📄 Preview of Extracted Text")
        st.text(full_text[:1000])  # show first 1000 characters
        st.success(f"Extracted {page_count} pages successfully.")
    else:
        st.error("❌ Failed to parse PDF.")
