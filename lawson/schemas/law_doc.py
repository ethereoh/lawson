from typing import List, Optional
from pydantic import BaseModel

from langchain_core.documents import Document
from lawson.schemas.base import BaseResponse


class LawsonFilter(BaseModel):
    splitter_type: str
    chunk_size: int
    chunk_overlap: int
    params: Optional[dict] = None


class LawsonResponse(BaseResponse):
    files: List[Document]
