class Coordinates:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column

    def __eq__(self, other: 'Coordinates') -> bool:
        if not isinstance(other, Coordinates):
            return NotImplemented
        return (self.row, self.column) == (other.row, other.column)

    def __repr__(self) -> str:
        return f"Coordinates({self.row},{self.column})"
