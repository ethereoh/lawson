from fastapi import APIRouter


router = APIRouter()


@router.post("/inference")
async def embed_data():
    pass
