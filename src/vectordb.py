"""
====================================================
FILE : vectordb.py
PROJECT : Enterprise-RAG-Assistant-v1.0
PURPOSE : ChromaDB Operations
AUTHOR : Devbrat Ghosh
====================================================
"""

import chromadb
from pathlib import Path

from src.config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME
)

from src.embeddings import model

from src.recursive_chunker import (
    load_text,
    recursive_chunk
)


# --------------------------------------------------
# CLIENT
# --------------------------------------------------
Path(CHROMA_DB_PATH).mkdir(

    parents=True,

    exist_ok=True,

)

client = chromadb.PersistentClient(

    path=str(CHROMA_DB_PATH)

)


# --------------------------------------------------
# COLLECTION
# --------------------------------------------------

def get_collection():
    # Fetch or create the collection
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    # First deployment / empty database
    if collection.count() == 0:
        print("Empty vector database detected.")
        print("Generating embeddings...")

        store_documents()

        # Refresh the collection after indexing
        collection = client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    return collection

# --------------------------------------------------
# RESET DATABASE
# --------------------------------------------------

def reset_collection():

    try:

        client.delete_collection(COLLECTION_NAME)

        print("Existing collection deleted.")

    except Exception:

        print("Collection does not exist. Creating a new one...")


# --------------------------------------------------
# LOAD CHUNKS
# --------------------------------------------------

def load_chunks():

    text = load_text()

    return recursive_chunk(text)


# --------------------------------------------------
# STORE DOCUMENTS
# --------------------------------------------------

def store_documents(
     chunks: list[str] | None = None,
    ):

    if chunks is None:

        chunks = load_chunks()

    collection = get_collection()

    ids: list[str] = []

    documents: list[str] = []

    embeddings: list[list[float]] = []

    print("Generating embeddings...")

    for i, chunk in enumerate(chunks):

        ids.append(f"chunk_{i}")

        documents.append(chunk)

        embeddings.append(

            model.encode(chunk).tolist()

        )

    collection.add(

        ids=ids,

        documents=documents,

        embeddings=embeddings

    )
    
    print()

    print(f"Stored {collection.count()} chunks.")
    
    return collection.count()


# --------------------------------------------------
# SEARCH
# --------------------------------------------------

def search(

        query: str,

        top_k: int = 3):

    collection = get_collection()

    query_embedding = model.encode(query).tolist()

    return collection.query(

        query_embeddings=[query_embedding],

        n_results=top_k

    )


# --------------------------------------------------
# TEST
# --------------------------------------------------

if __name__ == "__main__":

    reset_collection()
    
    print("[TRACE] Step 6 - Storing Vectors")
    
    store_documents()
    

    print()

    print("=" * 60)

    print("Semantic Search Test")

    print("=" * 60)

    results = search(

        "What is the leave policy?"

    )

    for i, doc in enumerate(

            results["documents"][0],

            start=1):

        print()

        print(f"Result {i}")

        print("-" * 40)

        print(doc[:400])