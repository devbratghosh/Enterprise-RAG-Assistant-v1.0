"""
============================================================
File      : report_builder.py
Project   : Enterprise-RAG-Assistant
Purpose   : Build markdown experiment reports.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from src.experiment.models import ChunkerExperiment
from src.experiment.experiment_events import ExperimentEvent

from src.core.markdown_writer import (
    heading,
    paragraph,
    horizontal_rule,
    bullet_list,
    markdown_table,
)


class ReportBuilder:
    """
    Builds markdown reports for chunking experiments.

    Responsibility:
        Convert experiment objects into markdown.

    This class does NOT:
        • Save files
        • Create directories
        • Update history
        • Log events
    """

    def __init__(self) -> None:

        self._content: list[str] = []


    # ======================================================
    # PUBLIC
    # ======================================================

    def build(
        self,
        experiment: ChunkerExperiment,
        events: list[ExperimentEvent],
    ) -> str:
        """
        Build complete markdown report.
        """

        self._content.clear()

        self._add_title()

        self._add_metadata(experiment)

        self._add_configuration(experiment)

        self._add_document_statistics(experiment)

        self._add_chunk_statistics(experiment)

        self._add_validation(experiment)

        self._add_events(events)

        self._add_notes(experiment)

        self._add_decision(experiment)

        return "".join(self._content)


    # ======================================================
    # TITLE
    # ======================================================

    def _add_title(self) -> None:

        self._content.append(

            heading(
                "Chunking Experiment Report"
            )

        )


    # ======================================================
    # METADATA
    # ======================================================

    def _add_metadata(
        self,
        experiment: ChunkerExperiment,
    ) -> None:

        self._content.append(

            heading(
                "Execution",
                level=2,
            )

        )

        rows = [

            ["Run", experiment.run_number],

            ["Date", experiment.execution_date],

            ["Time", experiment.execution_time],

            ["Duration (sec)", experiment.execution_duration],

        ]

        self._content.append(

            markdown_table(

                ["Property", "Value"],

                rows,

            )

        )

        self._content.append(

            horizontal_rule()

        )


    # ======================================================
    # CONFIGURATION
    # ======================================================

    def _add_configuration(
        self,
        experiment: ChunkerExperiment,
    ) -> None:

        config = experiment.configuration

        self._content.append(

            heading(
                "Configuration",
                level=2,
            )

        )

        rows = [

            ["Version", config.version],

            ["Strategy", config.strategy],

            ["Chunk Size", config.chunk_size],

            ["Overlap Strategy", config.overlap_strategy],

            ["Overlap Size", config.overlap_size],

            ["Embedding Model", config.embedding_model],

            ["Collection", config.collection_name],

            ["Top K", config.top_k],

        ]

        self._content.append(

            markdown_table(

                ["Setting", "Value"],

                rows,

            )

        )


    # ======================================================
    # DOCUMENT
    # ======================================================

    def _add_document_statistics(
        self,
        experiment: ChunkerExperiment,
    ) -> None:

        doc = experiment.document

        self._content.append(

            heading(
                "Document Statistics",
                level=2,
            )

        )

        rows = [

            ["Document", doc.document_name],

            ["Characters", doc.total_characters],

            ["Words", doc.total_words],

            ["Lines", doc.total_lines],

            ["Paragraphs", doc.total_paragraphs],

            ["Chapters", doc.total_chapters],

            ["Sections", doc.total_sections],

        ]

        self._content.append(

            markdown_table(

                ["Metric", "Value"],

                rows,

            )

        )


    # ======================================================
    # CHUNK STATS
    # ======================================================

    def _add_chunk_statistics(
        self,
        experiment: ChunkerExperiment,
    ) -> None:

        stats = experiment.chunk_statistics

        self._content.append(

            heading(
                "Chunk Statistics",
                level=2,
            )

        )

        rows = [

            ["Chunks", stats.total_chunks],

            ["Average Size", stats.average_chunk_size],

            ["Median Size", stats.median_chunk_size],

            ["Largest", stats.largest_chunk],

            ["Smallest", stats.smallest_chunk],

            ["Invalid", stats.invalid_chunks],

            ["Duplicate", stats.duplicate_chunks],

            ["Empty", stats.empty_chunks],

        ]

        self._content.append(

            markdown_table(

                ["Metric", "Value"],

                rows,

            )

        )


    # ======================================================
    # VALIDATION
    # ======================================================

    def _add_validation(
        self,
        experiment: ChunkerExperiment,
    ) -> None:

        validation = experiment.validation

        self._content.append(

            heading(
                "Validation",
                level=2,
            )

        )

        status = "PASSED" if validation.passed else "FAILED"

        self._content.append(

            paragraph(
                f"Overall Status: **{status}**"
            )

        )

        self._content.append(

            bullet_list(
                validation.messages
            )

        )


    # ======================================================
    # EVENTS
    # ======================================================

    def _add_events(
        self,
        events: list[ExperimentEvent],
    ) -> None:

        self._content.append(

            heading(
                "Execution Timeline",
                level=2,
            )

        )

        rows = []

        for event in events:

            rows.append(

                [

                    event.timestamp,

                    event.event_name,

                    event.description,

                ]

            )

        self._content.append(

            markdown_table(

                [

                    "Timestamp",

                    "Event",

                    "Description",

                ],

                rows,

            )

        )


    # ======================================================
    # NOTES
    # ======================================================

    def _add_notes(
        self,
        experiment: ChunkerExperiment,
    ) -> None:

        self._content.append(

            heading(
                "Engineering Notes",
                level=2,
            )

        )

        self._content.append(

            paragraph(
                experiment.engineering_notes
            )

        )

        self._content.append(

            heading(
                "Future Recommendation",
                level=2,
            )

        )

        self._content.append(

            paragraph(
                experiment.future_recommendation
            )

        )


    # ======================================================
    # DECISION
    # ======================================================

    def _add_decision(
        self,
        experiment: ChunkerExperiment,
    ) -> None:

        self._content.append(

            heading(
                "Engineering Decision",
                level=2,
            )

        )

        self._content.append(

            paragraph(
                f"**{experiment.decision}**"
            )

        )