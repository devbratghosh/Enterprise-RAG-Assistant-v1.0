"""
============================================================
File      : datetime_utils.py
Project   : Enterprise-RAG-Assistant
Purpose   : Date and time helper utilities.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from datetime import datetime

from src.core.constants import (
    DATE_FORMAT,
    TIME_FORMAT,
    DATETIME_FORMAT,
)


def current_datetime() -> datetime:
    """
    Return current local datetime.
    """

    return datetime.now()


def current_date() -> str:
    """
    Return formatted current date.
    """

    return current_datetime().strftime(
        DATE_FORMAT
    )


def current_time() -> str:
    """
    Return formatted current time.
    """

    return current_datetime().strftime(
        TIME_FORMAT
    )


def current_timestamp() -> str:
    """
    Return formatted date and time.
    """

    return current_datetime().strftime(
        DATETIME_FORMAT
    )