import os

import numpy as np
from PIL import ExifTags, Image

from src.modules.image_orientation.domain.models.images import ImageData
from src.modules.image_orientation.domain.models.paths import LocalDestinationPath, Path
from src.shared.errors import NotFoundError
from src.shared.interfaces import IFileAdapter

EXIF_ORIENTATION_TAG = ExifTags.Base.Orientation


class LocalFileAdapter(IFileAdapter):
    def get_image(self, source: Path) -> ImageData:
        image = Image.open(source.path)
        image.load()
        if not image:
            raise NotFoundError('Failed to read image from source path')
        image_exif = image.getexif()
        image_data = ImageData(
            pixels=np.array(image),
            metadata=image_exif,
            source_path=source,
        )
        return image_data

    def save_image(self, image: ImageData) -> str:
        destination_path = image.destination_path
        if not destination_path:
            destination_path = self._get_destination_path(image.source_path)
        pillow_image = Image.fromarray(image.pixels)
        pillow_image.save(destination_path.path, exif=image.metadata)
        return destination_path.path

    def _get_destination_path(self, source_path: Path) -> LocalDestinationPath:
        file, extension = os.path.splitext(source_path.path)
        destination = file + '_processed' + extension
        return LocalDestinationPath(path=destination)
