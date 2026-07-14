"""
============================================================
File      : history_repository.py
Project   : Enterprise-RAG-Assistant
Purpose   : Store and retrieve experiment history.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from pathlib import Path

from src.core.constants import (
    CHUNKER_HISTORY_FILE,
    CHUNK_HISTORY_HEADERS,
)

from src.core.csv_utils import (
    create_csv,
    append_row,
)

from src.core.filesystem import (
    file_exists,
    read_text,
)


class HistoryRepository:
    """
    Repository responsible for experiment history persistence.

    Responsibilities

    • Create history file
    • Read history
    • Append history
    • Generate next run id
    """

    def __init__(
        self,
        history_file: Path = CHUNKER_HISTORY_FILE,
    ) -> None:

        self.history_file = history_file

        self.initialize()


    # ------------------------------------------------------

    def initialize(self) -> None:
        """
        Create CSV if missing.
        """

        create_csv(

            self.history_file,

            CHUNK_HISTORY_HEADERS,

        )


    # ------------------------------------------------------

    def append(
        self,
        row: list,
    ) -> None:
        """
        Append one history record.
        """

        append_row(

            self.history_file,

            row,

        )


    # ------------------------------------------------------

    def total_runs(self) -> int:
        """
        Return total experiment count.
        """

        if not file_exists(
            self.history_file
        ):
            return 0

        lines = read_text(
            self.history_file
        ).splitlines()

        return max(

            0,

            len(lines) - 1,

        )


    # ------------------------------------------------------

    def next_run_number(self) -> int:
        """
        Return next experiment number.
        """

        return self.total_runs()


    # ------------------------------------------------------

    @staticmethod
    def format_run_number(
        run_number: int,
    ) -> str:
        """
        Format run number.

        Example

        000
        001
        """

        return f"{run_number:03d}"