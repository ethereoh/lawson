"This route is main route for RAG inference."

from fastapi import APIRouter

router = APIRouter()


@router.post("/inference")
async def rag_inference():
    """
    NOTE: last n-memories
    """
    pass


@router.post("/chat")
async def rag_chat():
    """
    NOTE: more features than `/inference`
    """
    pass
