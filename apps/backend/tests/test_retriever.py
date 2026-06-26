from vectorstore.retriever import Retriever


retriever = Retriever()

results = retriever.search(
    "Can I return a damaged Flipkart product?"
)

print("=" * 80)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")
    print("-" * 80)

    print("Score:", result.score)
    print("Document:", result.payload["document"])
    print("Page:", result.payload["page"])
    print("Domain:", result.payload["domain"])

    print("\nText:\n")
    print(result.payload["text"][:600])