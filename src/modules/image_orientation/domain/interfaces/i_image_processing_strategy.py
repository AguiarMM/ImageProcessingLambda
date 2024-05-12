from abc import ABC, abstractmethod
from src.shared.types import OpenCVImage


class IImageProcessingStrategy(ABC):
    @abstractmethod
    def execute(self, image: OpenCVImage) -> OpenCVImage:
        pass
