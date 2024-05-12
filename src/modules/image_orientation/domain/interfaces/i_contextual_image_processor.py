from abc import ABC, abstractmethod
from src.shared.types import OpenCVImage


class IContextualImageProcessor(ABC):
    @abstractmethod
    def process(self, image: OpenCVImage, document_type: str) -> OpenCVImage:
        pass
