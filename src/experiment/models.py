"""
============================================================
File      : models.py
Project   : Enterprise-RAG-Assistant
Purpose   : Data models used by the Experiment Framework.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from dataclasses import dataclass, field
from typing import List


# ==========================================================
# CONFIGURATION
# ==========================================================

@dataclass(slots=True)
class ChunkerConfiguration:
    """
    Chunker configuration used during an experiment.
    """

    version: str

    strategy: str

    chunk_size: int

    overlap_strategy: str

    overlap_size: int

    embedding_model: str

    collection_name: str

    top_k: int


# ==========================================================
# DOCUMENT STATISTICS
# ==========================================================

@dataclass(slots=True)
class DocumentStatistics:
    """
    Statistics collected from the input document.
    """

    document_name: str

    total_characters: int

    total_words: int

    total_lines: int

    total_paragraphs: int

    total_chapters: int

    total_sections: int

    empty_paragraphs_removed: int = 0

    duplicate_paragraphs_removed: int = 0


# ==========================================================
# CHUNK STATISTICS
# ==========================================================

@dataclass(slots=True)
class ChunkStatistics:
    """
    Statistics generated after chunking.
    """

    total_chunks: int

    average_chunk_size: float

    median_chunk_size: float

    smallest_chunk: int

    largest_chunk: int

    average_paragraphs_per_chunk: float

    invalid_chunks: int = 0

    empty_chunks: int = 0

    duplicate_chunks: int = 0

    chunks_with_chapter_title: int = 0

    chunks_with_section_title: int = 0

    chunks_starting_mid_sentence: int = 0

    chunks_ending_mid_sentence: int = 0


# ==========================================================
# VALIDATION RESULT
# ==========================================================

@dataclass(slots=True)
class ValidationResult:
    """
    Result of chunk validation.
    """

    passed: bool

    messages: List[str] = field(default_factory=list)


# ==========================================================
# EXPERIMENT
# ==========================================================

@dataclass(slots=True)
class ChunkerExperiment:
    """
    Complete experiment information.
    """

    run_number: int

    execution_date: str

    execution_time: str

    execution_duration: float

    configuration: ChunkerConfiguration

    document: DocumentStatistics

    chunk_statistics: ChunkStatistics

    validation: ValidationResult

    engineering_notes: str = ""

    future_recommendation: str = ""

    decision: str = "Needs Investigation"
    
    