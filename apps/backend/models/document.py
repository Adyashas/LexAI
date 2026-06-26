from pydantic import BaseModel


class DocumentPage(BaseModel):
    domain: str
    document: str
    source: str
    page: int
    text: str