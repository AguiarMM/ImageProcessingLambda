from src.shared.constants.status_codes import CONFLICT


class ConflictError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.status_code = CONFLICT
