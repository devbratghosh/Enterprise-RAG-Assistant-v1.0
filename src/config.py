"""
====================================================
FILE : config.py
PROJECT : Enterprise-RAG-Assistant-v1.0
PURPOSE : Central Configuration
AUTHOR : Devbrat Ghosh
====================================================
"""

from pathlib import Path

# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

PDF_FILE = DATA_DIR / "policy.pdf"

TEXT_FILE = DATA_DIR / "extracted_text.txt"

CHROMA_DB_PATH = BASE_DIR / "chroma_db"

# --------------------------------------------------
# CHUNKING
# --------------------------------------------------

CHUNK_SIZE = 800

CHUNK_OVERLAP = 100

# --------------------------------------------------
# EMBEDDINGS
# --------------------------------------------------

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# --------------------------------------------------
# VECTOR DATABASE
# --------------------------------------------------

COLLECTION_NAME = "enterprise_policies"

# --------------------------------------------------
# RETRIEVAL
# --------------------------------------------------

TOP_K_RESULTS = 3

# --------------------------------------------------
# STREAMLIT
# --------------------------------------------------

APP_TITLE = "Enterprise RAG Assistant"

APP_ICON = "📚"
