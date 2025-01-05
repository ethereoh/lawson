from lawson.schemas.base import BaseResponse, BaseRequest


class QARequest(BaseRequest):
    payload: str


# Keywords response may differ from QA response
class QAResponse(BaseResponse):
    payload: str
