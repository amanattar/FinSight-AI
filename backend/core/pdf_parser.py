import pdfplumber
import logging
import os

LOG_PATH = "./backend/logs/ingestion.log"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s %(message)s")

def extract_text_from_pdf(file_path: str, file_name: str):
    try:
        full_text = ""
        with pdfplumber.open(file_path) as pdf:
            page_count = len(pdf.pages)
            for page in pdf.pages:
                text = page.extract_text(x_tolerance=1, y_tolerance=1)
                if text:
                    full_text += text + "\n"

        logging.info(f"Uploaded: {file_name} — {page_count} pages parsed with pdfplumber.")
        return full_text, page_count

    except Exception as e:
        logging.error(f"Failed to parse {file_name} — {str(e)}")
        return None, 0
