"""
============================================================
File      : metadata_writer.py
Project   : Enterprise-RAG-Assistant
Purpose   : Generate experiment metadata JSON.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from dataclasses import asdict
from pathlib import Path

from src.core.filesystem import (
    write_json,
)

from src.core.constants import (
    CHUNKER_DIR,
)

from src.experiment.models import (
    ChunkerExperiment,
)

from src.experiment.history_repository import (
    HistoryRepository,
)


class MetadataWriter:
    """
    Generate metadata JSON for a chunking experiment.

    Responsibilities
    ----------------
    • Convert experiment object into JSON
    • Save metadata file

    This class does NOT

    • Generate reports
    • Update history
    • Export samples
    • Perform chunking
    """

    def __init__(
        self,
        metadata_directory: Path = CHUNKER_DIR / "metadata",
    ) -> None:

        self.metadata_directory = metadata_directory


    # ======================================================
    # PUBLIC
    # ======================================================

    def write(
        self,
        experiment: ChunkerExperiment,
    ) -> Path:
        """
        Write experiment metadata.

        Returns
        -------
        Path
            Metadata JSON file path.
        """

        run_id = HistoryRepository.format_run_number(
            experiment.run_number
        )

        file_path = (

            self.metadata_directory

            / f"{run_id}_metadata.json"

        )

        metadata = self._build_metadata(
            experiment
        )

        write_json(

            file_path=file_path,

            data=metadata,

        )

        return file_path


    # ======================================================
    # PRIVATE
    # ======================================================

    def _build_metadata(
        self,
        experiment: ChunkerExperiment,
    ) -> dict:
        """
        Build metadata dictionary.
        """

        return {

            "run_number":
                experiment.run_number,

            "execution": {

                "date":
                    experiment.execution_date,

                "time":
                    experiment.execution_time,

                "duration_seconds":
                    experiment.execution_duration,

            },

            "configuration":
                asdict(
                    experiment.configuration
                ),

            "document":
                asdict(
                    experiment.document
                ),

            "chunk_statistics":
                asdict(
                    experiment.chunk_statistics
                ),

            "validation":
                asdict(
                    experiment.validation
                ),

            "engineering_notes":
                experiment.engineering_notes,

            "future_recommendation":
                experiment.future_recommendation,

            "decision":
                experiment.decision,

        }