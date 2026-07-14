"""
============================================================
File      : base_builder.py
Purpose   : Base class for all builders.
============================================================
"""

from abc import ABC, abstractmethod


class BaseBuilder(ABC):
    """
    Base class for all builder classes.
    """

    @abstractmethod
    def build(self):
        """
        Build object.

        Returns
        -------
        Any
        """
        raise NotImplementedError