"""
============================================================
File      : base_event.py
Purpose   : Base event object.
============================================================
"""

from abc import ABC
from dataclasses import dataclass

from src.core.datetime_utils import current_timestamp


@dataclass(slots=True)
class BaseEvent(ABC):
    """
    Base event.
    """

    event_name: str

    description: str

    timestamp: str = ""

    def __post_init__(self):

        if not self.timestamp:

            self.timestamp = current_timestamp()