"""
============================================================
File      : statistics_builder.py
Project   : Enterprise-RAG-Assistant
Purpose   : Generate document, chunk and validation
            statistics for chunking experiments.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from __future__ import annotations
from dataclasses import dataclass
from email.mime import message
from pyexpat.errors import messages
from statistics import median
import re


from src.experiment.models import (
    DocumentStatistics,
    ChunkStatistics,
    ValidationResult,
)


# ==========================================================
# BUILD RESULT
# ==========================================================

@dataclass(slots=True)
class StatisticsResult:
    """
    Result returned by StatisticsBuilder.
    """

    document: DocumentStatistics

    chunk_statistics: ChunkStatistics

    validation: ValidationResult
    
    @property
    def experiment_components(
        self,
    ) -> tuple[
        DocumentStatistics,
        ChunkStatistics,
        ValidationResult,
    ]:
        """
        Convenience helper for experiment creation.
        """

        return (

            self.document,

            self.chunk_statistics,

            self.validation,

        )


# ==========================================================
# STATISTICS BUILDER
# ==========================================================

class StatisticsBuilder:
    """
    Build statistics used by the Experiment Framework.

    Responsibilities
    ----------------

    • Analyse source document

    • Analyse generated chunks

    • Validate chunk quality

    This class does NOT

    • Generate chunks

    • Generate embeddings

    • Save reports

    • Update history

    • Write files
    """

    # ======================================================
    # PUBLIC
    # ======================================================

    def build(
        self,
        document_name: str,
        text: str,
        chunks: list[str],
    ) -> StatisticsResult:
        """
        Build experiment statistics.
        """

        document = self._document_statistics(
            document_name=document_name,
            text=text,
        )

        chunk_statistics = self._chunk_statistics(
            chunks
        )

        validation = self._validation(
            chunks=chunks,
            statistics=chunk_statistics,
        )

        return StatisticsResult(

            document=document,

            chunk_statistics=chunk_statistics,

            validation=validation,

        )


    # ======================================================
    # DOCUMENT
    # ======================================================

    def _document_statistics(
        self,
        document_name: str,
        text: str,
    ) -> DocumentStatistics:
        """
        Analyse the source document.
        """
        # Pre-compute reusable collections
 
        text_words = text.split()

        text_lines = text.splitlines()
        
        paragraph_list = text.split("\n\n")
        
        characters = len(text)
        
        words = len(text_words)

        lines = len(text_lines)

        paragraphs = self._count_non_empty(paragraph_list)

        chapters = len(

            re.findall(

                r"(?im)^chapter\s+\d+",

                text,

            )

        )

        sections = len(

            re.findall(

                r"(?m)^\d+(\.\d+)+",

                text,

            )

        )

        return DocumentStatistics(

            document_name=document_name,

            total_characters=characters,

            total_words=words,

            total_lines=lines,

            total_paragraphs=paragraphs,

            total_chapters=chapters,

            total_sections=sections,

        )
        
    # ======================================================
    # CHUNK STATISTICS
    # ======================================================

    def _chunk_statistics(
        self,
        chunks: list[str],
    ) -> ChunkStatistics:
        """
        Analyse generated chunks.
        """

        if not chunks:

            return ChunkStatistics(

                total_chunks=0,

                average_chunk_size=0,

                median_chunk_size=0,

                smallest_chunk=0,

                largest_chunk=0,

                average_paragraphs_per_chunk=0,

            )

        chunk_sizes = [

            len(chunk)

            for chunk in chunks

        ]

        paragraph_counts =  [
            self._count_non_empty(chunk.split("\n\n"))
            for chunk in chunks
        ]

        duplicate_chunks = (

            len(chunks)

            - len(set(chunks))

        )

        empty_chunks = sum(

            1

            for chunk in chunks

            if not chunk.strip()

        )

        chapter_title_chunks = sum(

            1

            for chunk in chunks

            if re.search(

                r"(?im)^chapter\s+\d+",

                chunk,

            )

        )

        section_title_chunks = sum(

            1

            for chunk in chunks

            if re.search(

                r"(?m)^\d+(\.\d+)+",

                chunk,

            )

        )

        average_size = (

            sum(chunk_sizes)

            / len(chunk_sizes)

        )

        average_paragraphs = (

            sum(paragraph_counts)

            / len(paragraph_counts)

        )

        return ChunkStatistics(

            total_chunks=len(chunks),

            average_chunk_size=round(

                average_size,

                2,

            ),

            median_chunk_size=median(

                chunk_sizes,

            ),

            smallest_chunk=min(

                chunk_sizes,

            ),

            largest_chunk=max(

                chunk_sizes,

            ),

            average_paragraphs_per_chunk=round(

                average_paragraphs,

                2,

            ),

            duplicate_chunks=duplicate_chunks,

            empty_chunks=empty_chunks,

            chunks_with_chapter_title=chapter_title_chunks,

            chunks_with_section_title=section_title_chunks,

        )    
       
       
        # ======================================================
    # VALIDATION
    # ======================================================

    def _validation(
        self,
        chunks: list[str],
        statistics: ChunkStatistics,
    ) -> ValidationResult:
        """
        Validate generated chunks.
        """

        messages: list[str] = []

        invalid_chunks = 0

        starts_mid_sentence = 0

        ends_mid_sentence = 0

        for chunk in chunks:

            if not chunk.strip():

                invalid_chunks += 1

                continue

            if self._starts_mid_sentence(chunk):

                starts_mid_sentence += 1

            if self._ends_mid_sentence(chunk):

                ends_mid_sentence += 1

        statistics.invalid_chunks = invalid_chunks

        statistics.chunks_starting_mid_sentence = (

            starts_mid_sentence

        )

        statistics.chunks_ending_mid_sentence = (

            ends_mid_sentence

        )

        #
        # Validation Messages
        #

        if statistics.empty_chunks:

            messages.append(

                f"{statistics.empty_chunks} empty chunk(s) found."

            )

        if statistics.duplicate_chunks:

            messages.append(

                f"{statistics.duplicate_chunks} duplicate chunk(s) found."

            )

        if statistics.invalid_chunks:

            messages.append(

                f"{statistics.invalid_chunks} invalid chunk(s) found."

            )


        messages: list[str] = []
        warnings: list[str] = []
        
        if statistics.chunks_starting_mid_sentence:

            warnings.append(

               f"{statistics.chunks_starting_mid_sentence} chunk(s) start mid-sentence."

            )

        if statistics.chunks_ending_mid_sentence:

            warnings.append(

                f"{statistics.chunks_ending_mid_sentence} chunk(s) end mid-sentence."

            )
            
        passed = len(messages) == 0

        if passed:

            messages.append(

                "Validation completed successfully."

            )

        return ValidationResult(

            passed=passed,

            messages=messages,

        )


    # ======================================================
    # HELPERS
    # ======================================================

    def _starts_mid_sentence(
        self,
        chunk: str,
    ) -> bool:
        """
        Determine whether a chunk appears
        to begin in the middle of a sentence.
        """

        chunk = chunk.strip()

        if not chunk:

            return False

        first = chunk[0]
        
        # Simple heuristic.
        # Can be replaced by NLP in a future release.

        return first.islower()


    def _ends_mid_sentence(
        self,
        chunk: str,
    ) -> bool:
        """
        Determine whether a chunk appears
        to end in the middle of a sentence.
        """

        chunk = chunk.rstrip()

        if not chunk:

            return False

        return chunk[-1] not in ".!?)]\"'"


    def _count_non_empty(
        self,
        values: list[str],
    ) -> int:
        """
        Count non-empty values.
        """

        return sum(

            1

            for value in values

            if value.strip()

        )
             