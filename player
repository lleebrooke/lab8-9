from typing import Tuple

class Player:
    def __init__(self, start_row: int, start_col: int) -> None:
        self.row = start_row
        self.col = start_col
        self._blueberries_eaten = 0
        self._drank = False

    def eat(self) -> None:
        self._blueberries_eaten += 1

    def drank(self) -> None:
        self._drank = True

    def blueberries_eaten(self) -> int:
        return self._blueberries_eaten

    def has_drank(self) -> bool:
        return self._drank

    def position(self) -> Tuple[int,int]:
        return (self.row, self.col)

    def move(self, dr: int, dc: int) -> None:
        self.row += dr
        self.col += dc
