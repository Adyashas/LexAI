from pydantic import BaseModel

from models.chunk import DocumentChunk


class EmbeddingRecord(BaseModel):
    chunk: DocumentChunk
    vector: list[float]