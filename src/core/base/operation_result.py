"""
============================================================
File      : operation_result.py
Project   : Enterprise-RAG-Assistant
Purpose   : Standard operation result object.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class OperationResult:
    """
    Standard return object for framework operations.
    """

    success: bool

    message: str = ""

    data: Any | None = None

    error: Exception | None = None