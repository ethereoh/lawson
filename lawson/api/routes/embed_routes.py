from fastapi import APIRouter, HTTPException
from lawson.services.ai.embedding_service import EmbeddingService
from lawson.schemas.embed_schemas import EmbeddingRequest, EmbeddingResponse
from lawson.common.logging_config import setup_logger

# Initialize the router and logger
router = APIRouter()
logger = setup_logger("[EMBEDDING_SERVICE]")

# Initialize the embedding service
try:
    embed_service = EmbeddingService(model_name="your_model_name_here")
    logger.info("Embedding service initialized successfully.")
except Exception as e:
    logger.critical(f"Failed to initialize embedding service: {e}")
    raise RuntimeError("Embedding service initialization failed.") from e


@router.post(
    "/inference",
    status_code=200,
    response_model=EmbeddingResponse,
    summary="Generate embeddings from input payload",
    description="This endpoint generates embeddings for the given payload using the embedding model.",
    tags=["Embedding"],
)
async def embedding_inference(req: EmbeddingRequest):
    """
    Endpoint for generating embeddings.

    Args:
        req (EmbeddingRequest): The input payload for which embeddings need to be generated.

    Returns:
        EmbeddingResponse: The generated embeddings.
    """
    try:
        # Perform inference
        results = embed_service.inference(payload=req.payload)
        return EmbeddingResponse(embeddings=results)  # Ensure response matches schema
    except HTTPException as e:
        logger.error(f"HTTPException during inference: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error during inference: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")
