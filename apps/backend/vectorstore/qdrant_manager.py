from qdrant_client import QdrantClient

_client = QdrantClient(
    host="localhost",
    port=6333,
)


def get_client():
    return _client