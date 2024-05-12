import os

from pydantic import BaseModel, Field, field_validator

from src.shared.errors import NotFoundError
from src.shared.errors.validation_error import ValidationError


class Path(BaseModel):
    path: str = Field(min_length=1, frozen=True)


class LocalSourcePath(Path):
    @field_validator('path')
    def validate_source_path(cls, v: str) -> str:
        if not os.path.exists(v):
            raise NotFoundError('File does not exist')
        return v


class LocalDestinationPath(Path):
    @field_validator('path')
    def validate_destination_path(cls, v: str) -> str:
        directory, filename = os.path.split(v)
        _, extension = os.path.splitext(filename)
        if not os.path.exists(directory):
            raise NotFoundError('Destination directory does not exist')
        if not extension:
            raise ValidationError(
                'Missing file extension in destination path')
        return v
