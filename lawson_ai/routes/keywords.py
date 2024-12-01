from fastapi import APIRouter, HTTPException, Request, Response

from lawson_ai.api import __version__, get_keywords

kw_route = APIRouter(prefix=f"{__version__}/keywords")

from keybert import KeyBERT  # https://github.com/MaartenGr/KeyBERT

kw_model = KeyBERT()


@kw_route.post("/")
async def analyze_keywords(request: Request):
    try:
        response = await request.json()

        response = get_keywords(response, model=kw_model)

        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)
