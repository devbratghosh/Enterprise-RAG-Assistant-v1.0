"""
============================================================
File      : constants.py
Project   : Enterprise-RAG-Assistant
Purpose   : Central location for project constants.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from pathlib import Path

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ==========================================================
# PROJECT DIRECTORIES
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

DOCS_DIR = PROJECT_ROOT / "docs"

EVALUATION_DIR = PROJECT_ROOT / "evaluation"

# ==========================================================
# CHUNKER DIRECTORIES
# ==========================================================

CHUNKER_DIR = EVALUATION_DIR / "chunker"

CHUNKER_REPORTS_DIR = CHUNKER_DIR / "reports"

CHUNKER_SAMPLES_DIR = CHUNKER_DIR / "samples"

CHUNKER_METADATA_DIR = CHUNKER_DIR / "metadata"

CHUNKER_HISTORY_FILE = CHUNKER_DIR / "history.csv"

# ==========================================================
# RETRIEVAL DIRECTORIES
# ==========================================================

RETRIEVAL_DIR = EVALUATION_DIR / "retrieval"

RETRIEVAL_REPORTS_DIR = RETRIEVAL_DIR / "reports"

RETRIEVAL_METADATA_DIR = RETRIEVAL_DIR / "metadata"

RETRIEVAL_HISTORY_FILE = RETRIEVAL_DIR / "history.csv"

# ==========================================================
# GENERAL REPORT DIRECTORIES
# ==========================================================

REPORTS_DIR = EVALUATION_DIR / "reports"

EXPERIMENTS_DIR = EVALUATION_DIR / "experiments"

# ==========================================================
# SOURCE DOCUMENTS
# ==========================================================

POLICY_PDF = DATA_DIR / "policy.pdf"

EXTRACTED_TEXT = DATA_DIR / "extracted_text.txt"

# ==========================================================
# GENERATED FILE TEMPLATES
# ==========================================================

FIRST_CHUNK_TEMPLATE = "{run}_first_chunk.txt"

MIDDLE_CHUNK_TEMPLATE = "{run}_middle_chunk.txt"

LAST_CHUNK_TEMPLATE = "{run}_last_chunk.txt"

METADATA_TEMPLATE = "{run}_metadata.json"

REPORT_TEMPLATE = "{run}_chunk_report.md"

# ==========================================================
# FILE EXTENSIONS
# ==========================================================

REPORT_EXTENSION = ".md"

CSV_EXTENSION = ".csv"

TEXT_EXTENSION = ".txt"

JSON_EXTENSION = ".json"

# ==========================================================
# ENCODING
# ==========================================================

DEFAULT_ENCODING = "utf-8"

# ==========================================================
# DATE & TIME FORMAT
# ==========================================================

DATE_FORMAT = "%d-%b-%Y"

TIME_FORMAT = "%I:%M:%S %p"

DATETIME_FORMAT = "%d-%b-%Y %I:%M:%S %p"

# ==========================================================
# HISTORY CSV HEADERS
# ==========================================================

CHUNK_HISTORY_HEADERS = [

    "Run",

    "Version",

    "Date",

    "Time",

    "Document",

    "Strategy",

    "Chunk Size",

    "Overlap",

    "Chunks",

    "Average Size",

    "Largest",

    "Smallest",

    "Execution Time",

]

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def build_chunk_report_filename(run_id: str) -> str:
    """
    Return chunk report filename.

    Example
    -------
    000_chunk_report.md
    """

    return REPORT_TEMPLATE.format(run=run_id)


def build_metadata_filename(run_id: str) -> str:
    """
    Return metadata filename.

    Example
    -------
    000_metadata.json
    """

    return METADATA_TEMPLATE.format(run=run_id)


def build_first_chunk_filename(run_id: str) -> str:
    """
    Return first chunk sample filename.
    """

    return FIRST_CHUNK_TEMPLATE.format(run=run_id)


def build_middle_chunk_filename(run_id: str) -> str:
    """
    Return middle chunk sample filename.
    """

    return MIDDLE_CHUNK_TEMPLATE.format(run=run_id)


def build_last_chunk_filename(run_id: str) -> str:
    """
    Return last chunk sample filename.
    """

    return LAST_CHUNK_TEMPLATE.format(run=run_id)