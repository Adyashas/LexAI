from fastapi import APIRouter
from pydantic import BaseModel

from services.rag_service import RAGService

router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: AskRequest):
    rag = RAGService()
    return rag.ask(request.question)