from src.vectordb import search

results = search(
    "Corporate Vision",
    top_k=10
)

for i, doc in enumerate(results["documents"][0], start=1):

    print("=" * 80)
    print(f"Result {i}")
    print("=" * 80)
    print(doc)
    print()