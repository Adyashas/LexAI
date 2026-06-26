from vectorstore.retriever import Retriever
from generation.prompt_builder import PromptBuilder
from generation.gemini import GeminiGenerator


class RAGService:

    def __init__(self):
        self.retriever = Retriever()
        self.builder = PromptBuilder()
        self.generator = GeminiGenerator()

    def ask(self, question: str):

        chunks = self.retriever.search(
            question,
            limit=5
        )

        prompt = self.builder.build(
            question,
            chunks
        )

        answer = self.generator.generate(prompt)

        sources = []

        for chunk in chunks:
            sources.append({
                "document": chunk.payload["document"],
                "page": chunk.payload["page"],
                "domain": chunk.payload["domain"],
                "score": round(chunk.score, 3)
            })

        return {
            "answer": answer,
            "sources": sources
        }