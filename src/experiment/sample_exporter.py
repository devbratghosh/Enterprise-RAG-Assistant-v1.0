"""
============================================================
File      : sample_exporter.py
Project   : Enterprise-RAG-Assistant
Purpose   : Export representative chunk samples.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from pathlib import Path

from src.core.constants import (
    CHUNKER_SAMPLES_DIR,
)

from src.core.filesystem import (
    write_text,
)

from src.experiment.history_repository import (
    HistoryRepository,
)


class SampleExporter:
    """
    Export representative chunk samples.

    Responsibilities
    ----------------
    • Export first chunk
    • Export middle chunk
    • Export last chunk

    This class does NOT:

    • Generate chunks
    • Validate chunks
    • Write reports
    • Update history
    """

    def __init__(
        self,
        sample_directory: Path = CHUNKER_SAMPLES_DIR,
    ) -> None:

        self.sample_directory = sample_directory


    # ======================================================
    # PUBLIC
    # ======================================================

    def export(
        self,
        run_number: int,
        chunks: list[str],
    ) -> None:
        """
        Export representative chunk samples.

        Parameters
        ----------
        run_number
            Experiment run number.

        chunks
            Generated document chunks.
        """

        if not chunks:

            return

        run_id = HistoryRepository.format_run_number(
            run_number
        )

        self._write_sample(

            run_id,

            "first",

            chunks[0],

        )

        self._write_sample(

            run_id,

            "middle",

            chunks[
                len(chunks) // 2
            ],

        )

        self._write_sample(

            run_id,

            "last",

            chunks[-1],

        )


    # ======================================================
    # PRIVATE
    # ======================================================

    def _write_sample(
        self,
        run_id: str,
        sample_name: str,
        content: str,
    ) -> None:
        """
        Write one sample file.
        """

        file_path = (

            self.sample_directory

            / f"{run_id}_{sample_name}_chunk.txt"

        )

        write_text(

            file_path=file_path,

            content=content,

        )