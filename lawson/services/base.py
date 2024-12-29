from abc import ABC, abstractmethod
from typing import Any

# TODO: make response more generic
# TODO: strictly control service, add type service (AI inference, document process, storing data, etc.)


class BaseService(ABC):
    @abstractmethod
    def inference(self, *args, **kwargs) -> Any:
        raise NotImplementedError
