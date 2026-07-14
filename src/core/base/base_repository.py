"""
============================================================
File      : base_repository.py
Project   : Enterprise-RAG-Assistant
Purpose   : Generic repository interface.

Author    : Devbrat Ghosh
Version   : 1.1.0
============================================================
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    """
    Generic repository interface.
    """

    @abstractmethod
    def initialize(self) -> None:
        """
        Prepare repository.
        """
        raise NotImplementedError

    @abstractmethod
    def add(
        self,
        item: T,
    ) -> None:
        """
        Store one item.
        """
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        """
        Return total records.
        """
        raise NotImplementedError