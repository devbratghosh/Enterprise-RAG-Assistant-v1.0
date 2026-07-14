"""
============================================================
File      : enums.py
Project   : Enterprise-RAG-Assistant
Purpose   : Enumerations used throughout the Experiment
            Framework.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from enum import Enum


# ==========================================================
# EXPERIMENT STATUS
# ==========================================================

class ExperimentStatus(str, Enum):
    """
    Current execution status.
    """

    DRAFT = "Draft"

    RUNNING = "Running"

    COMPLETED = "Completed"

    FAILED = "Failed"

    FROZEN = "Frozen"


# ==========================================================
# ENGINEERING DECISION
# ==========================================================

class EngineeringDecision(str, Enum):
    """
    Final engineering decision after evaluation.
    """

    ACCEPTED = "Accepted"

    REJECTED = "Rejected"

    NEEDS_INVESTIGATION = "Needs Investigation"

    EXPERIMENTAL = "Experimental"

    DEPRECATED = "Deprecated"


# ==========================================================
# OVERLAP STRATEGY
# ==========================================================

class OverlapStrategy(str, Enum):
    """
    Supported overlap strategies.
    """

    NONE = "None"

    CHARACTER = "Character"

    PARAGRAPH = "Paragraph"

    SENTENCE = "Sentence"


# ==========================================================
# CHUNK STRATEGY
# ==========================================================

class ChunkStrategy(str, Enum):
    """
    Supported chunking strategies.
    """

    FIXED = "Fixed"

    RECURSIVE = "Recursive"

    DOCUMENT_AWARE = "Document Aware"

    SEMANTIC = "Semantic"


# ==========================================================
# VALIDATION STATUS
# ==========================================================

class ValidationStatus(str, Enum):
    """
    Validation result.
    """

    PASSED = "Passed"

    WARNING = "Warning"

    FAILED = "Failed"