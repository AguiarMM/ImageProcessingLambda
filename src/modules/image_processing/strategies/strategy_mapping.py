from images.face_orientation_strategy import FaceOrientationStrategy
from images.text_orientation_strategy import TextOrientationStrategy
from ..constants.documents_types import IDENTIFICATION_DOCUMENT_BACK, IDENTIFICATION_DOCUMENT_FRONT, SELFIE_WITH_DOCUMENT


strategy_mapping = {
    IDENTIFICATION_DOCUMENT_FRONT: TextOrientationStrategy(),
    IDENTIFICATION_DOCUMENT_BACK: TextOrientationStrategy(),
    SELFIE_WITH_DOCUMENT: FaceOrientationStrategy()
}
