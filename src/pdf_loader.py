"""
====================================================
FILE : pdf_loader.py
PROJECT : Enterprise-RAG-Assistant-v1.0
PURPOSE : Extract and Clean PDF Text
AUTHOR : Dev + ChatGPT
====================================================
"""

import re
import PyPDF2

from src.config import PDF_FILE, TEXT_FILE


# --------------------------------------------------
# CLEAN TEXT
# --------------------------------------------------

def clean_text(text: str) -> str:
    """
    Clean extracted PDF text.
    """

    text = text.replace("", "- ")
    text = text.replace("\t", " ")

    text = re.sub(r" +", " ", text)

    text = re.sub(
        r"(\d+\.\d+)",
        r"\n\1",
        text
    )

    return text.strip()


# --------------------------------------------------
# EXTRACT TEXT
# --------------------------------------------------

def extract_pdf_text() -> str:
    """
    Extract text from PDF.
    """

    text = ""

    with open(PDF_FILE, "rb") as pdf:

        reader = PyPDF2.PdfReader(pdf)

        print(f"Pages Found : {len(reader.pages)}")

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return clean_text(text)


# --------------------------------------------------
# SAVE TEXT
# --------------------------------------------------

def save_text(text: str):

    TEXT_FILE.write_text(

        text,

        encoding="utf-8"

    )


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def process_pdf():

    text = extract_pdf_text()

    save_text(text)

    print()

    print("PDF successfully processed.")

    print(f"Characters : {len(text):,}")

    print(f"Saved To   : {TEXT_FILE}")


if __name__ == "__main__":

    process_pdf()
