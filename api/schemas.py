from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    question: str

class Citation(BaseModel):
    source: str
    chunk_id: str

class QueryResponse(BaseModel):
    answer: str
    citations: List[Citation]
    confidence: float
