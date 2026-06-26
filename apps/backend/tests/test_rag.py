from vectorstore.retriever import Retriever
from generation.prompt_builder import PromptBuilder
from generation.gemini import GeminiGenerator


def main():

    question = input("\nAsk your legal question:\n> ")

    retriever = Retriever()

    chunks = retriever.search(
        question,
        limit=5
    )

    builder = PromptBuilder()

    prompt = builder.build(
        question,
        chunks
    )

    generator = GeminiGenerator()

    answer = generator.generate(
        prompt
    )

    print("\n")
    print("=" * 80)

    print(answer)

    print("=" * 80)

    print("\nSources\n")

    for chunk in chunks:

        print(
            f"{chunk.payload['document']} | "
            f"Page {chunk.payload['page']} | "
            f"Score {chunk.score:.3f}"
        )


if __name__ == "__main__":
    main()