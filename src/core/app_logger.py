"""
============================================================
File      : app_logger.py
Project   : Enterprise-RAG-Assistant
Purpose   : Common application logger.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

import logging
from pathlib import Path

from src.core.filesystem import ensure_directory


# ==========================================================
# LOGGER
# ==========================================================

def get_logger(
    name: str,
    log_directory: Path | None = None,
) -> logging.Logger:
    """
    Return a configured logger.
    """

    logger = logging.getLogger(name)

    if logger.handlers:

        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)-8s | %(message)s",

        "%d-%b-%Y %I:%M:%S %p",

    )

    console = logging.StreamHandler()

    console.setFormatter(formatter)

    logger.addHandler(console)

    if log_directory is not None:

        ensure_directory(log_directory)

        log_file = log_directory / f"{name}.log"

        file_handler = logging.FileHandler(

            log_file,

            encoding="utf-8",

        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    logger.propagate = False

    return logger