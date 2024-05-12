from typing import Any

import pytest
from pydantic import ValidationError as PydanticValidationError

from src.modules.image_orientation.domain.models.paths import LocalDestinationPath
from src.shared.errors import NotFoundError, ValidationError


class TestLocalDestinationPath:
    def test_correct_creation_of_local_destination_path(self):
        existing_directory_path = 'tests/unit/modules/image_orientation/samples/image.png'
        local_destination_path = LocalDestinationPath(
            path=existing_directory_path)
        assert isinstance(local_destination_path, LocalDestinationPath)
        assert local_destination_path.path == existing_directory_path

    def test_local_destination_path_immutability(self):
        existing_directory_path = 'tests/unit/modules/image_orientation/samples/image.png'
        local_destination_path = LocalDestinationPath(
            path=existing_directory_path)
        with pytest.raises(PydanticValidationError):
            local_destination_path.path = 'tests/unit/modules/image_orientation/samples/new_image.png'

    def test_validation_error_raised_for_invalid_path(self):
        invalid_file_paths: Any = [3, None, '', {}, [], ()]
        for invalid_file_path in invalid_file_paths:
            with pytest.raises(PydanticValidationError):
                LocalDestinationPath(path=invalid_file_path)

    def test_not_found_error_raised_for_non_existing_path(self):
        non_existing_file_path = 'tests/unit/modules/image_orientation/samples/non_existing_directory/image.png'
        with pytest.raises(NotFoundError):
            LocalDestinationPath(path=non_existing_file_path)

    def test_validation_error_raised_for_invalid_file_name(self):
        invalid_file_path: Any = 'tests/unit/modules/image_orientation/samples/image'
        with pytest.raises(ValidationError):
            LocalDestinationPath(path=invalid_file_path)
