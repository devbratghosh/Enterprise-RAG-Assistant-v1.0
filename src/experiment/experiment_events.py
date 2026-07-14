"""
============================================================
File      : experiment_events.py
Project   : Enterprise-RAG-Assistant
Purpose   : Experiment event definitions.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from dataclasses import dataclass

from src.core.datetime_utils import current_timestamp


@dataclass(slots=True)
class ExperimentEvent:
    """
    Represents a single experiment event.
    """

    event_name: str

    description: str

    timestamp: str = ""


    def __post_init__(self) -> None:

        if not self.timestamp:

            self.timestamp = current_timestamp()


# ==========================================================
# FACTORY FUNCTIONS
# ==========================================================

def chunking_started() -> ExperimentEvent:

    return ExperimentEvent(

        event_name="Chunking Started",

        description="Chunk generation started.",

    )


def chunking_completed() -> ExperimentEvent:

    return ExperimentEvent(

        event_name="Chunking Completed",

        description="Chunk generation completed.",

    )


def validation_started() -> ExperimentEvent:

    return ExperimentEvent(

        event_name="Validation Started",

        description="Chunk validation started.",

    )


def validation_completed() -> ExperimentEvent:

    return ExperimentEvent(

        event_name="Validation Completed",

        description="Chunk validation completed.",

    )


def report_generated() -> ExperimentEvent:

    return ExperimentEvent(

        event_name="Report Generated",

        description="Markdown report generated.",

    )


def history_updated() -> ExperimentEvent:

    return ExperimentEvent(

        event_name="History Updated",

        description="Experiment history updated.",

    )