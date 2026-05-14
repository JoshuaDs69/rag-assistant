from fastapi import APIRouter

from src.app.db.chroma_client import get_collection
from src.app.rag.pipeline import RAGPipeline
from src.app.schemas.query import QueryRequest

router = APIRouter()


collection = get_collection()

pipeline = RAGPipeline(collection)


@router.post("/ask")
def ask_question(payload: QueryRequest):

    result = pipeline.ask(payload.query)

    return result
