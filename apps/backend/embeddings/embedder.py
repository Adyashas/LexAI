from sentence_transformers import SentenceTransformer

from models.chunk import DocumentChunk
from models.embedding import EmbeddingRecord


class Embedder:

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            "BAAI/bge-base-en-v1.5"
        )

        print("Embedding model loaded.")

    def embed(
        self,
        chunks: list[DocumentChunk]
    ) -> list[EmbeddingRecord]:

        texts = [
            chunk.text
            for chunk in chunks
        ]

        vectors = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        records = []

        for chunk, vector in zip(chunks, vectors):

            records.append(
                EmbeddingRecord(
                    chunk=chunk,
                    vector=vector.tolist()
                )
            )

        return records