from fastapi import APIRouter
from api.schemas import QueryRequest, QueryResponse

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
def query_knowledge_base(request: QueryRequest):
    response = rag_engine.answer(request.question)
    return response
