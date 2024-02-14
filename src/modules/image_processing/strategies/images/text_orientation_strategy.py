import pytesseract
import cv2
import imutils

from src.shared.types import OpenCVImage
from src.modules.image_processing.interfaces import IImageProcessingStrategy


class TextOrientationStrategy(IImageProcessingStrategy):
    def execute(self, image: OpenCVImage) -> OpenCVImage:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pytesseract.image_to_osd(
            rgb, output_type=pytesseract.Output.DICT)
        assert isinstance(
            results, dict), f"Expected a dictionary, got {type(results)}"
        rotated = imutils.rotate_bound(image, angle=results['rotate'])
        return rotated
