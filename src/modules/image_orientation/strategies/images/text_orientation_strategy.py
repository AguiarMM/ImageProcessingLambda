import cv2
import pytesseract
from pytesseract import Output

from src.shared.types import OpenCVImage
from src.modules.image_processing.interfaces import IImageProcessingStrategy


class TextOrientationStrategy(IImageProcessingStrategy):
    def execute(self, image: OpenCVImage) -> OpenCVImage:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        required_rotation = pytesseract.image_to_osd(
            rgb_image, output_type=Output.DICT, nice=1)
        print(required_rotation)
        return image
