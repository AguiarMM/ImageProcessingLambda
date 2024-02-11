from shared.types import OpenCVImage
from ...interfaces import IImageProcessingStrategy


class TextOrientationStrategy(IImageProcessingStrategy):
    def execute(self, image: OpenCVImage) -> OpenCVImage:
        pass
