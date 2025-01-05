from typing import Optional
from pydantic import BaseModel


# TODO: Add more type checking method


class BaseRequest(BaseModel):
    payload: Optional[str] = None


class BaseResponse(BaseModel):
    model_name: Optional[str] = None
    response_time: Optional[int]  # Measure in seconds
    total_length: Optional[int]
