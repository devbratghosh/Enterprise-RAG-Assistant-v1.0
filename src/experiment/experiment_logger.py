"""
============================================================
File      : experiment_logger.py
Project   : Enterprise-RAG-Assistant
Purpose   : Coordinate experiment execution and artifact
            generation.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from __future__ import annotations

from pathlib import Path
from time import perf_counter

from src.core.constants import (
    CHUNKER_REPORTS_DIR,
    build_chunk_report_filename,
)

from src.core.markdown_writer import (
    save_markdown,
)

from src.experiment.models import (
    ChunkerExperiment,
)

from src.experiment.experiment_events import (
    ExperimentEvent,
    chunking_started,
    chunking_completed,
    validation_started,
    validation_completed,
    report_generated,
    history_updated,
)

from src.experiment.history_repository import (
    HistoryRepository,
)

from src.experiment.report_builder import (
    ReportBuilder,
)

from src.experiment.sample_exporter import (
    SampleExporter,
)

from src.experiment.metadata_writer import (
    MetadataWriter,
)


class ExperimentLogger:
    """
    Coordinate the complete experiment lifecycle.

    Responsibilities
    ----------------

    • Manage execution events

    • Record execution duration

    • Update history

    • Generate metadata

    • Export chunk samples

    • Generate markdown reports

    This class intentionally contains
    no chunking logic and no retrieval logic.
    """
    
    def __init__(
        self,
        history: HistoryRepository | None = None,
        report_builder: ReportBuilder | None = None,
        sample_exporter: SampleExporter | None = None,
        metadata_writer: MetadataWriter | None = None,
        report_directory: Path = CHUNKER_REPORTS_DIR,
        
    ) -> None:

        self.history = history or HistoryRepository()

        self.report_builder = (
            report_builder
            or ReportBuilder()
        )

        self.sample_exporter = (
            sample_exporter
            or SampleExporter()
        )

        self.metadata_writer = (
            metadata_writer
            or MetadataWriter()
        )

        self.report_directory = report_directory

        self._events: list[ExperimentEvent] = []

        self._started: float = 0.0

        self._finished: float = 0.0


    # ======================================================
    # PUBLIC
    # ======================================================

    def start(self) -> None:
        """
        Start experiment timing.
        """

        self._events.clear()

        self._started = perf_counter()

        self.add_event(
            chunking_started()
        )


    def add_event(
        self,
        event: ExperimentEvent,
    ) -> None:
        """
        Add one experiment event.
        """

        self._events.append(event)


    @property
    def events(
        self,
    ) -> list[ExperimentEvent]:
        """
        Return experiment events.
        """

        return list(self._events)


    def execution_duration(self) -> float:
        """
        Return execution duration.

        Returns
        -------
        float
            Seconds.
        """

        self._finished = perf_counter()

        return round(

            self._finished

            - self._started,

            3,

        )
        
    # ======================================================
    # COMPLETE EXPERIMENT
    # ======================================================

    def complete(
        self,
        experiment: ChunkerExperiment,
        chunks: list[str],
    ) -> tuple[ChunkerExperiment, list[ExperimentEvent]]:
        """
        Complete experiment execution.

        Generates:

        • history
        • chunk samples
        • metadata
        • markdown report

        Returns
        -------
        tuple
            (experiment, events)
        """

        #
        # Finish timing
        #

        experiment.execution_duration = (

            self.execution_duration()

        )

        #
        # Chunking Complete
        #

        self.add_event(

            chunking_completed()

        )

        #
        # Validation Complete
        #

        self.add_event(

            validation_completed()

        )

        #
        # Update History
        #

        self._update_history(
            experiment
        )

        self.add_event(

            history_updated()

        )

        #
        # Export Samples
        #

        self.sample_exporter.export(

            experiment.run_number,

            chunks,

        )

        #
        # Metadata
        #

        self.metadata_writer.write(

            experiment

        )

        #
        # Markdown Report
        #

        self.add_event(

            report_generated()

        )

        self._generate_report(

            experiment

        )

        return (

            experiment,

            self.events,

        )


    # ======================================================
    # HISTORY
    # ======================================================

    def _update_history(
        self,
        experiment: ChunkerExperiment,
    ) -> None:
        """
        Append experiment history.
        """

        config = experiment.configuration

        stats = experiment.chunk_statistics

        document = experiment.document

        self.history.append(

            [

                experiment.run_number,

                config.version,

                experiment.execution_date,

                experiment.execution_time,

                document.document_name,

                config.strategy,

                config.chunk_size,

                config.overlap_size,

                stats.total_chunks,

                stats.average_chunk_size,

                stats.largest_chunk,

                stats.smallest_chunk,

                experiment.execution_duration,

            ]

        )    
        
        
        # ======================================================
    # REPORT
    # ======================================================

    def _generate_report(
        self,
        experiment: ChunkerExperiment,
    ) -> None:
        """
        Generate and save markdown report.
        """

        report = self.report_builder.build(

            experiment,

            self.events,

        )

        save_markdown(

            file_path=self._report_path(

                experiment.run_number

            ),

            content=report,

        )


    # ======================================================
    # REPORT PATH
    # ======================================================

    def _report_path(
        self,
        run_number: int,
    ) -> Path:
        """
        Return report path.

        Example
        -------
        evaluation/
            chunker/
                reports/
                    000_chunk_report.md
        """

        run_id = HistoryRepository.format_run_number(

            run_number,

        )

        filename = build_chunk_report_filename(

            run_id,

        )

        return (

            self.report_directory

            / filename

        )    
        
        