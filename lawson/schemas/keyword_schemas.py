from typing import List

from lawson.schemas.base import BaseResponse, BaseRequest


class KeywordRequest(BaseRequest):
    payload: str


class KeywordsResponse(BaseResponse):
    payload: List[str]  # Extracted keywords
    conf: List[float]  # Confidence scores
