from typing import List, Union

from pydantic import BaseModel


class PayloadRequest(BaseModel):
    payload: str


class PayloadResponse(BaseModel):
    model_name: str = None
    response_time: int  # Measure in seconds
    total_length: int


# Keywords response may differ from QA response
class QAResponse(PayloadResponse):
    payload: str


class KeywordsResponse(PayloadResponse):
    payloads: List[str]  # Extracted keywords
    conf: List[float]  # Confidence scores
