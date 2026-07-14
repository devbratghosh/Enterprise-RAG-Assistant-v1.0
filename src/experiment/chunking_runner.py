"""
============================================================
File      : chunking_runner.py
Project   : Enterprise-RAG-Assistant
Purpose   : Execute a complete chunking experiment.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from __future__ import annotations

from src.core.constants import POLICY_PDF
from src.config import (
    EMBEDDING_MODEL,
    COLLECTION_NAME,
    TOP_K_RESULTS,
)

from src.recursive_chunker import (
    load_text,
)

from src.vectordb import (
    load_chunks,
    store_documents,
)

from src.core.datetime_utils import (
    current_date,
    current_time,
)

from src.experiment.models import (
    ChunkerConfiguration,
    ChunkerExperiment,
)

from src.experiment.history_repository import (
    HistoryRepository,
)

from src.experiment.statistics_builder import (
    StatisticsBuilder,
)

from src.experiment.experiment_logger import (
    ExperimentLogger,
)


class ChunkingRunner:
    """
    Execute a complete chunking experiment.

    Responsibilities
    ----------------

    • Load source document

    • Generate chunks

    • Build statistics

    • Create experiment object

    • Store vectors

    • Finalize experiment

    This class intentionally contains
    no chunking logic, embedding logic
    or reporting logic.
    """

    def __init__(
        self,
        statistics_builder: StatisticsBuilder | None = None,
        experiment_logger: ExperimentLogger | None = None,
        history: HistoryRepository | None = None,
    ) -> None:

        self.statistics_builder = (

            statistics_builder

            or StatisticsBuilder()

        )

        self.logger = (

            experiment_logger

            or ExperimentLogger()

        )

        self.history = (

            history

            or HistoryRepository()

        )

    # ======================================================
    # PUBLIC
    # ======================================================

    def run(
        self,
        configuration: ChunkerConfiguration,
        document_name: str,
    ) -> ChunkerExperiment:
        """
        Execute a complete chunking experiment.
        """

        #
        # Start experiment
        #

        self.logger.start()

        #
        # Load document
        #

        text = load_text()

        #
        # Generate chunks
        #

        chunks = load_chunks()

        #
        # Analyse chunks
        #

        statistics = self.statistics_builder.build(

            document_name=document_name,

            text=text,

            chunks=chunks,

        )

        #
        # Create experiment
        #

        experiment = ChunkerExperiment(

            run_number=self.history.next_run_number(),

            execution_date=current_date(),

            execution_time=current_time(),

            execution_duration=0.0,

            configuration=configuration,

            document=statistics.document,

            chunk_statistics=statistics.chunk_statistics,

            validation=statistics.validation,

        )
        
            #
        # Store vectors
        #

        stored_chunks = store_documents(

            chunks=chunks,

        )

        #
        # Complete experiment
        #

        experiment, _ = self.logger.complete(

            experiment=experiment,

            chunks=chunks,

        )

        #
        # Integrity Check
        #
        
        if stored_chunks != (

            experiment.chunk_statistics.total_chunks

        ):

            raise RuntimeError(

                "Chunk count mismatch between "

                "Experiment Framework "

                "and Vector Database."

            )
            
        print("ChunkingRunner finished successfully.")
        
        return experiment    
        
# ======================================================
# MAIN
# ======================================================

if __name__ == "__main__":

    configuration = ChunkerConfiguration(

        version="1.0.0",

        strategy="Recursive",

        chunk_size=500,

        overlap_strategy="Section Boundary",

        overlap_size=50,

        embedding_model=EMBEDDING_MODEL,

        collection_name=COLLECTION_NAME,

        top_k=TOP_K_RESULTS,

    )

    runner = ChunkingRunner()

    experiment = runner.run(

        configuration=configuration,

        document_name=  POLICY_PDF.name,

    )

    print("\n" + "=" * 60)
    print("Chunking Experiment Completed")
    print("=" * 60)
    print(f"Run Number      : {experiment.run_number:03d}")
    print(f"Chunks          : {experiment.chunk_statistics.total_chunks}")
    print(f"Duration        : {experiment.execution_duration:.3f} sec")
    print(f"Validation      : {'PASSED' if experiment.validation.passed else 'FAILED'}")        