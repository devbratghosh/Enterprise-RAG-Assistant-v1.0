"""
====================================================
FILE : rag_query.py
PROJECT : Enterprise-RAG-Assistant-v1.0
PURPOSE : Enterprise RAG Query Engine
AUTHOR : Devbrat Ghosh
====================================================
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from src.config import TOP_K_RESULTS
from src.vectordb import search


# ==================================================
# LOAD ENVIRONMENT
# ==================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = ROOT_DIR / ".env"

#
# Local Development
#
# Load .env only if it exists.
#

if ENV_FILE.exists():

    load_dotenv(

        dotenv_path=ENV_FILE,

        override=True,

    )

#
# Docker / Production
#
# Environment variables are supplied by Docker.
# 


# ==================================================
# CONFIGURATION
# ==================================================

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "openrouter/free")


# ==================================================
# OPENROUTER CLIENT
# ==================================================

_client = None


def get_client():
    """
    Create the OpenRouter client only when required.
    """

    global _client

    if _client is None:

        if not API_KEY:

            raise RuntimeError(
                "\nOPENROUTER_API_KEY was not loaded.\n"
                "Please check your .env file."
            )

        _client = OpenAI(
            api_key=API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    return _client


# ==================================================
# BUILD PROMPT
# ==================================================

def build_prompt(question: str, documents: list[str]) -> str:
    """
    Build the prompt sent to the LLM.
    """

    context = "\n\n".join(documents)

    return f"""
You are an Enterprise Knowledge Assistant.

Answer ONLY from the supplied context.

If the answer cannot be found in the supplied context,
reply exactly:

"I could not find this information in the knowledge base."

Do not invent facts.

If possible, mention the relevant policy section.

------------------------------------------------
CONTEXT
------------------------------------------------

{context}

------------------------------------------------
QUESTION
------------------------------------------------

{question}

------------------------------------------------
ANSWER
------------------------------------------------
"""


# ==================================================
# ASK LLM
# ==================================================

def ask_llm(prompt: str) -> str:
    """
    Send prompt to OpenRouter.
    """

    client = get_client()

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


# ==================================================
# COMPLETE RAG
# ==================================================

def ask(question: str) -> dict:
    """
    Complete RAG pipeline.
    """

    results = search(
        question,
        top_k=TOP_K_RESULTS
    )

    documents = results["documents"][0]

    prompt = build_prompt(
        question,
        documents
    )

    answer = ask_llm(prompt)

    return {
        "question": question,
        "answer": answer,
        "documents": documents
    }


# ==================================================
# CLI TEST
# ==================================================

def main():

    print("=" * 60)
    print("Enterprise RAG Assistant")
    print("=" * 60)

    print(f"Model : {MODEL_NAME}")

    while True:

        question = input("\nAsk : ").strip()

        if question.lower() in ["exit", "quit"]:
            break

        if not question:
            continue

        try:

            result = ask(question)

            print("\nAnswer\n")
            print(result["answer"])

        except Exception as ex:

            print("\nERROR")
            print(ex)


if __name__ == "__main__":
    main()