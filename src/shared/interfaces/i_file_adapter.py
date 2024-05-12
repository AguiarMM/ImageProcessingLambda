from abc import ABC, abstractmethod

from src.modules.image_orientation.domain.models.images import ImageData
from src.modules.image_orientation.domain.models.paths import Path


class IFileAdapter(ABC):
    @abstractmethod
    def get_image(self, source: Path) -> ImageData:
        ...

    @abstractmethod
    def save_image(self, image: ImageData) -> str:
        ...
