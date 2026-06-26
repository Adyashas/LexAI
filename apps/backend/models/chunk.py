from pydantic import BaseModel


class DocumentChunk(BaseModel):
    domain: str
    document: str
    source: str
    page: int
    chunk_id: str
    text: str