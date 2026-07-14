 """
============================================================
File      : base_logger.py
Project   : Enterprise-RAG-Assistant
Purpose   : Generic logger interface.

Author    : Devbrat Ghosh
Version   : 1.1.0
============================================================
"""

from abc import ABC, abstractmethod

from src.core.base.operation_result import OperationResult


class BaseLogger(ABC):
    """
    Parent class for framework loggers.
    """

    @abstractmethod
    def log(self, *args, **kwargs) -> OperationResult:
        """
        Execute logging operation.
        """
        raise NotImplementedError