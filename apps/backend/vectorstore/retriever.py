from sentence_transformers import SentenceTransformer

from vectorstore.qdrant_manager import get_client
from vectorstore.indexer import Indexer


class Retriever:

    def __init__(self):
        self.client = get_client()

        self.model = SentenceTransformer(
            "BAAI/bge-base-en-v1.5"
        )

    def search(
        self,
        query: str,
        limit: int = 5
    ):

        query_vector = self.model.encode(
            query,
            normalize_embeddings=True
        ).tolist()

        results = self.client.query_points(
            collection_name=Indexer.COLLECTION,
            query=query_vector,
            limit=limit,
        )

        return results.points