"""
============================================================
File      : base_report_builder.py
Purpose   : Base class for report builders.
============================================================
"""

from abc import ABC, abstractmethod


class BaseReportBuilder(ABC):
    """
    Base report builder.
    """

    @abstractmethod
    def build(self, *args, **kwargs) -> str:
        """
        Build report.
        """
        raise NotImplementedError