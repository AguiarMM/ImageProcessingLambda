from src.shared.interfaces import IUseCase, IFileAdapter
from typing import TypedDict

from src.modules.image_processing.interfaces import IContextualImageProcessor


class Params(TypedDict):
    image_source: str
    document_type: str


class Result(TypedDict):
    image_destination: str


class FixImageOrientationUseCase(IUseCase[Params, Result]):
    def __init__(self, contextual_image_processor: IContextualImageProcessor, file_adapter: IFileAdapter):
        self.contextual_image_processor = contextual_image_processor
        self.file_adapter = file_adapter

    def execute(self, params: Params) -> Result:
        image_source = params['image_source']
        document_type = params['document_type']
        image = self.file_adapter.get_image(image_source)
        processed_image = self.contextual_image_processor.process(
            image, document_type
        )
        image_destination = self.file_adapter.save_image(processed_image)
        return {'image_destination': image_destination}
