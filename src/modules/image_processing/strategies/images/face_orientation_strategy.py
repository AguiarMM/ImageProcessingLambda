from shared.types import OpenCVImage
from ...interfaces import IImageProcessingStrategy


class FaceOrientationStrategy(IImageProcessingStrategy):
    def execute(self, image: OpenCVImage) -> OpenCVImage:
        pass
