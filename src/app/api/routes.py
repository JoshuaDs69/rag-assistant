from fastapi import APIRouter

from src.app.db.chroma_client import get_collection
from src.app.rag.pipeline import RAGPipeline


router = APIRouter()


collection = get_collection()

pipeline = RAGPipeline(collection)


@router.post("/ask")
def ask_question(payload: dict):

    query = payload["query"]

    result = pipeline.ask(query)

    return result
