from qdrant_client.models import Distance, PointStruct, VectorParams

from models.embedding import EmbeddingRecord
from vectorstore.qdrant_manager import get_client


class Indexer:
    COLLECTION = "legal_documents"

    def __init__(self):
        self.client = get_client()

    def create_collection(self):
        collections = self.client.get_collections().collections
        names = [collection.name for collection in collections]

        if self.COLLECTION not in names:
            self.client.create_collection(
                collection_name=self.COLLECTION,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE,
                ),
            )
            print("Collection created.")
        else:
            print("Collection already exists.")

    def index(self, records: list[EmbeddingRecord]):
        points = []

        for idx, record in enumerate(records):
            points.append(
                PointStruct(
                    id=idx,
                    vector=record.vector,
                    payload={
                        "text": record.chunk.text,
                        "document": record.chunk.document,
                        "page": record.chunk.page,
                        "domain": record.chunk.domain,
                        "source": record.chunk.source,
                        "chunk_id": record.chunk.chunk_id,
                    },
                )
            )

        self.client.upsert(
            collection_name=self.COLLECTION,
            points=points,
        )

        print(f"Indexed {len(points)} chunks.")