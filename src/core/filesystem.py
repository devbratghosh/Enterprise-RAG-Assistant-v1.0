"""
============================================================
File      : filesystem.py
Project   : Enterprise-RAG-Assistant
Purpose   : Common filesystem utilities.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from pathlib import Path
import json
from typing import Any

from src.core.constants import DEFAULT_ENCODING
from src.core.exceptions import (
    DirectoryCreationError,
    FileReadError,
    FileWriteError,
)


# ==========================================================
# DIRECTORY FUNCTIONS
# ==========================================================


def ensure_directory(directory: Path) -> None:
    """
    Create directory if it does not already exist.
    """

    try:

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    except Exception as exc:

        raise DirectoryCreationError(
            f"Unable to create directory: {directory}"
        ) from exc


# ==========================================================
# FILE EXISTENCE
# ==========================================================


def file_exists(file_path: Path) -> bool:
    """
    Check whether a file exists.
    """

    return file_path.exists()


# ==========================================================
# TEXT FILES
# ==========================================================


def read_text(file_path: Path) -> str:
    """
    Read text file.
    """

    try:

        return file_path.read_text(
            encoding=DEFAULT_ENCODING
        )

    except Exception as exc:

        raise FileReadError(
            f"Unable to read file: {file_path}"
        ) from exc


def write_text(
    file_path: Path,
    content: str,
) -> None:
    """
    Write text file.
    """

    ensure_directory(file_path.parent)

    try:

        file_path.write_text(
            content,
            encoding=DEFAULT_ENCODING,
        )

    except Exception as exc:

        raise FileWriteError(
            f"Unable to write file: {file_path}"
        ) from exc


def append_text(
    file_path: Path,
    content: str,
) -> None:
    """
    Append text to an existing file.
    """

    ensure_directory(file_path.parent)

    try:

        with open(
            file_path,
            "a",
            encoding=DEFAULT_ENCODING,
        ) as file:

            file.write(content)

    except Exception as exc:

        raise FileWriteError(
            f"Unable to append file: {file_path}"
        ) from exc


# ==========================================================
# JSON
# ==========================================================


def write_json(
    file_path: Path,
    data: Any,
    indent: int = 4,
) -> None:
    """
    Write JSON file.
    """

    ensure_directory(file_path.parent)

    try:

        with open(
            file_path,
            "w",
            encoding=DEFAULT_ENCODING,
        ) as file:

            json.dump(
                data,
                file,
                indent=indent,
                ensure_ascii=False,
            )

    except Exception as exc:

        raise FileWriteError(
            f"Unable to write JSON: {file_path}"
        ) from exc


def read_json(file_path: Path) -> Any:
    """
    Read JSON file.
    """

    try:

        with open(
            file_path,
            "r",
            encoding=DEFAULT_ENCODING,
        ) as file:

            return json.load(file)

    except Exception as exc:

        raise FileReadError(
            f"Unable to read JSON: {file_path}"
        ) from exc


# ==========================================================
# DELETE
# ==========================================================


def delete_file(file_path: Path) -> None:
    """
    Delete file if it exists.
    """

    if file_path.exists():

        file_path.unlink()


# ==========================================================
# LIST FILES
# ==========================================================


def list_files(
    directory: Path,
    pattern: str = "*",
) -> list[Path]:
    """
    Return sorted list of files.
    """

    if not directory.exists():

        return []

    return sorted(directory.glob(pattern))


# ==========================================================
# FILE SIZE
# ==========================================================


def file_size(file_path: Path) -> int:
    """
    Return file size in bytes.
    """

    return file_path.stat().st_size


# ==========================================================
# STEM
# ==========================================================


def file_stem(file_path: Path) -> str:
    """
    Return filename without extension.
    """

    return file_path.stem


# ==========================================================
# SUFFIX
# ==========================================================


def file_extension(file_path: Path) -> str:
    """
    Return file extension.
    """

    return file_path.suffix