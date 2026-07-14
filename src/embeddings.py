"""
====================================================
FILE : embeddings.py
PROJECT : Enterprise-RAG-Assistant-v1.0
PURPOSE : Embedding Model Loader
AUTHOR : Devbrat Ghosh
====================================================
"""

from sentence_transformers import SentenceTransformer

from src.config import EMBEDDING_MODEL


print("Loading embedding model...")

model = SentenceTransformer(

    EMBEDDING_MODEL

)

print("Embedding model loaded successfully.")