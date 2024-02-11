from interfaces import IContextualImageProcessor, IImageProcessingStrategy
from src.shared.types import OpenCVImage
from ..strategies.strategy_mapping import strategy_mapping
from typing import Mapping


class ContextualImageProcessor(IContextualImageProcessor):
    def __init__(self, strategies: Mapping[str, IImageProcessingStrategy] = strategy_mapping):
        self.strategies = strategies

    def process(self, image: OpenCVImage, document_type: str) -> OpenCVImage:
        strategy = self.strategies[document_type]
        processed_image = strategy.execute(image)
        return processed_image
