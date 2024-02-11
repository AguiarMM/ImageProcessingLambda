from src.shared.constants.status_codes import NOT_FOUND


class NotFoundError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.status_code = NOT_FOUND
