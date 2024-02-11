from abc import ABC, abstractmethod
from src.shared.types import OpenCVImage


class IFileAdapter(ABC):
    @abstractmethod
    def get_image(self, source: str) -> OpenCVImage:
        pass

    @abstractmethod
    def save_image(self, image: OpenCVImage) -> str:
        pass
