"""
====================================================
FILE : recursive_chunker.py
PROJECT : Enterprise-RAG-Assistant-v1.1
PURPOSE : Document Aware Recursive Chunker
AUTHOR : Devbrat Ghosh
====================================================
"""

import re

from src.config import (
    TEXT_FILE,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


# --------------------------------------------------
# LOAD DOCUMENT
# --------------------------------------------------

def load_text():

    with open(
        TEXT_FILE,
        encoding="utf-8"
    ) as f:

        return f.read()


# --------------------------------------------------
# SPLIT LARGE PARAGRAPH
# --------------------------------------------------

def split_large_paragraph(
        paragraph,
        chunk_size):

    words = paragraph.split()

    chunks = []

    current = ""

    for word in words:

        if len(current) + len(word) + 1 <= chunk_size:

            current += word + " "

        else:

            chunks.append(
                current.strip()
            )

            current = word + " "

    if current.strip():

        chunks.append(
            current.strip()
        )

    return chunks


# --------------------------------------------------
# PREPROCESS DOCUMENT
# --------------------------------------------------

def preprocess_document(text):

    """
    Merge document header
    with Chapter 1.

    This prevents the
    first semantic topic
    from being split.
    """

    match = re.search(

        r"Chapter\s+1",

        text,

        flags=re.IGNORECASE

    )

    if not match:

        return text

    header = text[:match.start()].strip()

    chapter_text = text[match.start():]

    return (

        header

        + "\n\n"

        + chapter_text

    )


# --------------------------------------------------
# CHAPTER SPLIT
# --------------------------------------------------

def split_chapters(text):

    return re.split(

        r"(?=Chapter\s+\d+)",

        text,

        flags=re.IGNORECASE

    )


# --------------------------------------------------
# BUILD CHUNKS
# --------------------------------------------------

def recursive_chunk(text):

    text = preprocess_document(text)

    chapters = split_chapters(text)

    chapters = [

        c.strip()

        for c in chapters

        if c.strip()

    ]

    final_chunks = []

    for chapter in chapters:

        lines = [

            line.strip()

            for line in chapter.split("\n")

            if line.strip()

        ]

        if not lines:

            continue

        chapter_title = lines[0]

        current_chunk = chapter_title + "\n\n"

        for paragraph in lines[1:]:

            # --------------------------
            # Preserve Section Headings
            # --------------------------

            if re.match(

                r"^\d+(\.\d+)+",

                paragraph

            ):

                paragraph = "\n" + paragraph

            # --------------------------

            if len(paragraph) > CHUNK_SIZE:

                if current_chunk.strip():

                    final_chunks.append(

                        current_chunk.strip()

                    )

                parts = split_large_paragraph(

                    paragraph,

                    CHUNK_SIZE

                )

                for part in parts:

                    final_chunks.append(

                        chapter_title

                        + "\n\n"

                        + part

                    )

                current_chunk = chapter_title + "\n\n"

                continue

            if (

                len(current_chunk)

                + len(paragraph)

                <= CHUNK_SIZE

            ):

                current_chunk += (

                    paragraph

                    + "\n\n"

                )

            else:

                final_chunks.append(

                    current_chunk.strip()

                )

                overlap = current_chunk[

                    -CHUNK_OVERLAP:

                ]

                current_chunk = (

                    chapter_title

                    + "\n\n"

                    + overlap

                    + "\n\n"

                    + paragraph

                    + "\n\n"

                )

        if current_chunk.strip():

            final_chunks.append(

                current_chunk.strip()

            )

    return final_chunks


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    text = load_text()

    chunks = recursive_chunk(text)

    print()

    print("=" * 60)

    print(

        "Total Chunks :",

        len(chunks)

    )

    print("=" * 60)

    print()

    print(chunks[0])

    print()

    print("=" * 60)