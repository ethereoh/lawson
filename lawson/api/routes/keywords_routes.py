from fastapi import APIRouter

router = APIRouter()


@router.post("/inference")
async def keywords_inference():
    pass
