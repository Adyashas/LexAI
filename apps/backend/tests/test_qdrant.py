from vectorstore.qdrant_manager import QdrantManager

client = QdrantManager().get_client()

collections = client.get_collections()

print(collections)