from src.shared.constants.status_codes import UNPROCESSABLE_ENTITY


class ValidationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.status_code = UNPROCESSABLE_ENTITY
