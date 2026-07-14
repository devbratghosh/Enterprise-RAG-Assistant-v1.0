"""
============================================================
File      : markdown_writer.py
Project   : Enterprise-RAG-Assistant
Purpose   : Markdown report generation utilities.

Author    : Devbrat Ghosh
Version   : 1.0.0
============================================================
"""

from pathlib import Path
from typing import Iterable

from src.core.filesystem import write_text


# ==========================================================
# TITLE
# ==========================================================

def heading(
    text: str,
    level: int = 1,
) -> str:
    """
    Return a markdown heading.
    """

    level = max(1, min(level, 6))

    return f'{"#" * level} {text}\n\n'


# ==========================================================
# PARAGRAPH
# ==========================================================

def paragraph(text: str) -> str:
    """
    Return a markdown paragraph.
    """

    return f"{text}\n\n"


# ==========================================================
# HORIZONTAL RULE
# ==========================================================

def horizontal_rule() -> str:
    """
    Return a markdown horizontal rule.
    """

    return "---\n\n"


# ==========================================================
# BULLET LIST
# ==========================================================

def bullet_list(items: Iterable[str]) -> str:
    """
    Return a markdown bullet list.
    """

    lines = []

    for item in items:

        lines.append(f"- {item}")

    return "\n".join(lines) + "\n\n"


# ==========================================================
# TABLE
# ==========================================================

def markdown_table(
    headers: list[str],
    rows: list[list],
) -> str:
    """
    Create a markdown table.
    """

    output = ""

    output += "| " + " | ".join(headers) + " |\n"

    output += "|"

    output += "|".join(["---"] * len(headers))

    output += "|\n"

    for row in rows:

        output += "| "

        output += " | ".join(
            str(value)
            for value in row
        )

        output += " |\n"

    output += "\n"

    return output


# ==========================================================
# SAVE REPORT
# ==========================================================

def save_markdown(
    file_path: Path,
    content: str,
) -> None:
    """
    Save markdown report.
    """

    write_text(
        file_path=file_path,
        content=content,
    )