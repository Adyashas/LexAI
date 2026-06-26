from generation.gemini import GeminiGenerator


def main():
    generator = GeminiGenerator()

    response = generator.generate(
        "Say hello in one sentence."
    )

    print(response)


if __name__ == "__main__":
    main()