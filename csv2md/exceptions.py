class BaseError(Exception):
    pass


class ColumnIdentifierError(BaseError):
    def __init__(self, column):
        msg = f'Invalid column identifier "{column}". Must be non-negative integer or range of non-negative integers separated by "-".'
        super().__init__(msg)
