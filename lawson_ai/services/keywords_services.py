from datetime import datetime

from lawson_ai.schemas import KeywordsResponse, PayloadRequest


def get_keywords(payload: PayloadRequest, model) -> KeywordsResponse:
    try:
        response = KeywordsResponse()
        start_time = datetime.now()
        keywords = model.extract_keywords(payload)  # return : list[(keyword, conf)]
        end_time = datetime.now()
        elapsed_time = end_time - start_time

        response.response_time = elapsed_time
        response.payloads = [k[0] for k in keywords]
        response.conf = [k[1] for k in keywords]
        response.total_length = len(response.payloads)

        return response
    except Exception as e:
        raise e
