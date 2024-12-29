"This route is main route for RAG inference."

from fastapi import APIRouter

router = APIRouter()


@router.post("/inference")
async def rag_inference():
    pass
