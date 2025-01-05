from sentence_transformers import SentenceTransformer
from lawson.services.base import BaseAIService
from lawson.common.logging_config import setup_logger
from lawson.core.config import app_settings
from lawson.common.strategy import measure_execution
from lawson.schemas.embed_schemas import EmbeddingResponse

# Set up logging
logger = setup_logger(name="[EMBEDDING_SERVICE]")


class EmbeddingService(BaseAIService):
    """
    A service for generating embeddings using SentenceTransformer.
    """

    def __init__(
        self, model_name: str = "all-MiniLM-L6-v2", device: str = None, *args, **kwargs
    ):
        """
        Initialize the embedding service.

        Args:
            model_name (str): Name of the SentenceTransformer model.
            device (str, optional): Device to use ('cpu', 'cuda', etc.). Defaults to app_settings.DEVICE.
        """
        self.model_name = model_name
        self.device = device or app_settings.DEVICE
        self.model = self._initialize_model()

    def _initialize_model(self) -> SentenceTransformer:
        """
        Initializes the SentenceTransformer model.

        Returns:
            SentenceTransformer: The initialized model.

        Raises:
            ValueError: If the model cannot be initialized.
        """
        try:
            model = SentenceTransformer(self.model_name, device=self.device)
            logger.info(
                f"Model '{self.model_name}' initialized successfully on {self.device}."
            )
            return model
        except Exception as e:
            logger.critical(f"Failed to initialize model '{self.model_name}': {e}")
            raise ValueError(
                f"Model '{self.model_name}' is invalid or could not be loaded."
            ) from e

    def inference(self, payload: str | list[str], **kwargs) -> EmbeddingResponse:
        """
        Encodes the input text into embeddings.

        Args:
            payload (str | list[str]): Input text or list of texts for embedding.
            **kwargs: Additional keyword arguments for the encoder.

        Returns:
            EmbeddingResponse: The generated embeddings and metadata.
        """
        try:
            # Measure execution time and encode the input
            result = measure_execution(
                func=self.model.encode, sentences=payload, **kwargs
            )
            embeddings = result.get("result").tolist()  # Convert numpy array to list

            # Build response
            response = EmbeddingResponse(
                embeddings=embeddings,
                execution_time=result.get("execution_time"),
                description=self.describe(),
            )
            logger.info(f"Embedding inference successful for payload: {payload}")
            return response
        except Exception as e:
            logger.error(f"Error during embedding inference: {e}")
            raise ValueError("Failed to generate embeddings.") from e

    def describe(self) -> dict:
        """
        Provides metadata about the embedding model.

        Returns:
            dict: Description of the model including name, device, and specifications.
        """
        try:
            description = {
                "model_name": self.model_name,
                "device": self.device,
                "max_seq_length": self.model.get_max_seq_length(),
                "embedding_shape": self.model.get_sentence_embedding_dimension(),
                "backend": self.model.get_backend(),
            }
            logger.debug(f"Model description: {description}")
            return description
        except Exception as e:
            logger.error(f"Error fetching model description: {e}")
            raise RuntimeError("Failed to retrieve model description.") from e


# TODO: Add Huggingface model's pool to widen the choices.
