import pytest

from lawson.common.logging_config import setup_logger
from lawson.services.ai.embedding_service import EmbeddingService

logger = setup_logger("[TESTER]")


@pytest.fixture
def init_embedding_service():
    return EmbeddingService(model_name="all-MiniLM-L6-v2", device="cuda")
