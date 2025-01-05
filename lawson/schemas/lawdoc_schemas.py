from typing import List, Optional
from pydantic import BaseModel

from langchain_core.documents import Document
from lawson.schemas.base import BaseResponse, BaseRequest


class LawsonFilter(BaseModel):
    splitter_type: str
    chunk_size: int
    chunk_overlap: int
    params: Optional[dict] = None


class DocLoaderRequest(BaseRequest):
    pass


class DocLoaderResponse(BaseResponse):
    files: List[Document]
