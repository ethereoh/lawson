from abc import ABC, abstractmethod
from typing import Any

# TODO: make response more generic
# TODO: strictly control service, add type service (AI inference, document process, storing data, etc.)


class BaseService(ABC):
    @abstractmethod
    def inference(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class BaseAIService(BaseService):
    @abstractmethod
    def _init_model(self, model_name: str) -> Any:
        raise NotImplementedError

    @abstractmethod
    def describe(self) -> dict:
        raise NotImplementedError


class BaseVectorDBService(ABC):
    """Base class for services that is in charge of interacting with VectorDB, including:
    1. Basic CRUD.
    2. Vector search or hybrid search if the provider allows (Milvus, ChromaDB, etc.)
    """

    @abstractmethod
    def create(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def insert(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def update(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs) -> Any:
        raise NotImplementedError

    @abstractmethod
    def search(self, *args, **kwargs) -> Any:
        raise NotImplementedError
