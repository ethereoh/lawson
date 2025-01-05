from typing import List

import numpy as np
from pydantic import field_validator
from lawson.schemas.base import BaseResponse, BaseRequest


class EmbeddingRequest(BaseRequest):
    payload: str | List[str]


class EmbeddingResponse(BaseResponse):
    payload: list
    description: dict

    @field_validator("payload", mode="before")
    def convert_nparray_to_list(cls, value):
        if isinstance(value, np.ndarray):
            value = value.tolist()
        return value
