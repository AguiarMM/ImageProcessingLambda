import cv2
import os

from datetime import datetime
from src.shared.types import OpenCVImage
from src.shared.interfaces import IFileAdapter
from src.shared.errors import ValidationError, NotFoundError, ConflictError
from typing import Any


class LocalFileAdapter(IFileAdapter):
    def get_image(self, source: str) -> OpenCVImage:
        self._validate_source_path(source)
        image = cv2.imread(source)
        if not image.size:
            raise NotFoundError('Failed to read image from source path')
        return image

    def save_image(self, image: OpenCVImage) -> str:
        destination = self._get_destination_path()
        success = cv2.imwrite(destination, image)
        if not success:
            raise ConflictError('Failed to write image to destination path')
        return destination

    def _get_destination_path(self) -> str:
        root = os.getcwd()
        sub_directory = 'resources/processed_images'
        full_directory_path = os.path.join(root, sub_directory)

        if not os.path.exists(full_directory_path):
            os.makedirs(full_directory_path)

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename_pattern = f"{timestamp}_processed_image.png"
        full_save_path = os.path.join(full_directory_path, filename_pattern)
        return full_save_path

    def _validate_source_path(self, path: Any) -> None:
        is_string = isinstance(path, str)
        if not is_string:
            raise ValidationError(
                'Source path of image must be a string')
        is_file = os.path.isfile(path)
        if not is_file:
            raise ValidationError('Source must point to an existing file')
