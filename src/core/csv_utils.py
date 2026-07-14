"""
============================================================
File      : csv_utils.py
Project   : Enterprise-RAG-Assistant
Purpose   : Common CSV helper utilities.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from __future__ import annotations

import csv
from pathlib import Path

from src.core.constants import DEFAULT_ENCODING
from src.core.filesystem import ensure_directory


# ==========================================================
# CREATE CSV
# ==========================================================

def create_csv(
    file_path: Path,
    headers: list[str],
) -> None:
    """
    Create a CSV file with a header row if it does not exist.
    """

    if file_path.exists():
        return

    ensure_directory(file_path.parent)

    with open(
        file_path,
        "w",
        newline="",
        encoding=DEFAULT_ENCODING,
    ) as file:

        writer = csv.writer(file)
        writer.writerow(headers)


# ==========================================================
# APPEND ROW
# ==========================================================

def append_row(
    file_path: Path,
    row: list,
) -> None:
    """
    Append a row to a CSV file.
    """

    ensure_directory(file_path.parent)

    with open(
        file_path,
        "a",
        newline="",
        encoding=DEFAULT_ENCODING,
    ) as file:

        writer = csv.writer(file)
        writer.writerow(row)


# ==========================================================
# READ CSV
# ==========================================================

def read_csv(
    file_path: Path,
) -> list[list[str]]:
    """
    Read all rows from a CSV file.
    """

    if not file_path.exists():
        return []

    with open(
        file_path,
        "r",
        newline="",
        encoding=DEFAULT_ENCODING,
    ) as file:

        return list(csv.reader(file))