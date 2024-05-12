from typing import Optional

from numpy import generic, typing
from PIL import Image
from pydantic import BaseModel, ConfigDict

from src.modules.image_orientation.domain.models.paths import Path


class ImageData(BaseModel):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)

    pixels: typing.NDArray[generic]
    metadata: Image.Exif
    source_path: Path
    destination_path: Optional[Path] = None
