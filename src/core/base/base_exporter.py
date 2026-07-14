"""
============================================================
File      : base_exporter.py
Purpose   : Base exporter.
============================================================
"""

from abc import ABC, abstractmethod


class BaseExporter(ABC):
    """
    Base exporter.
    """

    @abstractmethod
    def export(self, *args, **kwargs):
        """
        Export data.
        """
        raise NotImplementedError