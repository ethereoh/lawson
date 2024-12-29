from fastapi import APIRouter


router = APIRouter()


@router.post("/inference")
async def qa_inference():
    pass
