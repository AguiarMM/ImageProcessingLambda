from typing import Any

import pytest
from pydantic import ValidationError

from src.modules.image_orientation.domain.models.paths import LocalSourcePath
from src.shared.errors.not_found_error import NotFoundError


class TestLocalSourcePath:
    def test_correct_creation_of_local_source_path(self):
        existing_file_path = 'tests/unit/modules/image_orientation/samples/id_document_correct.png'
        local_source_path = LocalSourcePath(path=existing_file_path)
        assert isinstance(local_source_path, LocalSourcePath)
        assert local_source_path.path == existing_file_path

    def test_local_source_path_immutability(self):
        existing_file_path = 'tests/unit/modules/image_orientation/samples/id_document_correct.png'
        local_source_path = LocalSourcePath(path=existing_file_path)
        with pytest.raises(ValidationError):
            local_source_path.path = 'tests/unit/modules/image_orientation/samples/new_image.png'

    def test_validation_error_raised_for_invalid_path(self):
        invalid_file_paths: Any = [3, None, '', {}, [], ()]
        for invalid_file_path in invalid_file_paths:
            with pytest.raises(ValidationError):
                LocalSourcePath(path=invalid_file_path)

    def test_not_found_error_raised_for_non_existing_path(self):
        non_existing_file_path = 'tests/unit/modules/image_orientation/samples/id_document_incorrect.png'
        with pytest.raises(NotFoundError):
            LocalSourcePath(path=non_existing_file_path)
