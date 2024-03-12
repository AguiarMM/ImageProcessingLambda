from abc import ABC, abstractmethod
from src.shared.types import OpenCVImage
from typing import Any


class IFileAdapter(ABC):
    @abstractmethod
    def get_image(self, source: str) -> OpenCVImage:
        ...

    @abstractmethod
    def save_image(self, image: OpenCVImage, saveParams: Any = {}) -> str:
        ...
