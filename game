import random
from typing import List, Tuple
from forestpatch import ForestPatch
from blueberrybush import BlueberryBush
from pond import Pond
from deerherd import DeerHerd
from bearden import BearDen
from player import Player

class Game:
    def __init__(self) -> None:
        self.rows = 5
        self.cols = 5
        self.forest: List[List[ForestPatch]] = [[ForestPatch() for _ in range(self.cols)] for _ in range(self.rows)]
        # Place fixed events
        # Coordinates: row 0 top, row 4 bottom. Column 0 left, column 4 right.
        self.place_event(0, 4, Pond())
        self.place_event(0, 0, BlueberryBush())
        self.place_event(4, 4, BlueberryBush())
        self.place_event(4, 0, DeerHerd())
        # Place 3 bear dens in random empty patches (not occupied already)
        empty_coords = [(r,c) for r in range(self.rows) for c in range(self.cols) if self.forest[r][c].get_event() is None]
        bear_positions = random.sample(empty_coords, 3)
        for r,c in bear_positions:
            self.place_event(r, c, BearDen())
        # Create player at bottom-left (4,0)
        self.player = Player(4,0)
        # keep previous location for bear back-move
        self._prev_pos = (4,0)
        self._game_over = False

    def place_event(self, r: int, c: int, event) -> None:
        self.forest[r][c].set_event(event)

    def print_forest(self) -> None:
        sep = '-' * (self.cols*3 + (self.cols+1))
        for r in range(self.rows):
            print(sep)
            row_str = '|'
            for c in range(self.cols):
                patch = self.forest[r][c]
                # Determine display: if player here, show * plus event symbol (two chars total)
                if (r,c) == (self.player.row, self.player.col):
                    ev = patch.get_event()
                    symbol = ev.symbol() if ev is not None else ' '
                    row_str += f"*{symbol}|"
                else:
                    row_str += f" {patch.symbol()}|"
            print(row_str)
        print(sep)

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def handle_encounter(self, r: int, c: int) -> None:
        patch = self.forest[r][c]
        ev = patch.get_event()
        if ev is None:
            return
        # Call the encounter method; some events signal removal by returning True
        remove = ev.encounter(self.player)
        # Special handling for bear den: if first encounter, move player back to previous pos.
        if isinstance(ev, BearDen):
            # If first encounter, we already printed the "Whew..." message inside BearDen
            # Move back if this was the first encounter (we detect by checking prev_pos differs from current)
            # We rely on BearDen's internal counter for printing and logic.
            # If the bear den's encounters >1, it's game over.
            # To know whether it's game over, call again: check if last printed message was game over by checking player's state
            # Simpler: if ev._encounters >=2 then mark game over.
            if getattr(ev, "_encounters", 0) == 1:
                # move back
                self.player.row, self.player.col = self._prev_pos
            elif getattr(ev, "_encounters", 0) >= 2:
                self._game_over = True
        else:
            # Non-bear events: if they return True, remove the event from the patch (bush eaten)
            if remove:
                patch.remove_event()
            # DeerHerd: if player meets conditions, end game
            if isinstance(ev, DeerHerd):
                if self.player.has_drank() and self.player.blueberries_eaten() >= 2:
                    self._game_over = True

    def prompt_move(self) -> Tuple[int,int]:
        while True:
            ans = input("Where would you like to go? (Use W/A/S/D to move): ").strip().lower()
            if ans not in ('w','a','s','d'):
                print('Invalid input')
                continue
            dr, dc = 0,0
            if ans == 'w':
                dr = -1
            elif ans == 's':
                dr = 1
            elif ans == 'a':
                dc = -1
            elif ans == 'd':
                dc = 1
            newr = self.player.row + dr
            newc = self.player.col + dc
            if not self.in_bounds(newr,newc):
                print('Invalid direction!')
                continue
            return (dr,dc)

    def run(self) -> None:
        # Print initial forest
        self.print_forest()
        while not self._game_over:
            dr, dc = self.prompt_move()
            # store previous position
            self._prev_pos = (self.player.row, self.player.col)
            # move player
            self.player.move(dr, dc)
            # handle encounter if any
            self.handle_encounter(self.player.row, self.player.col)
            # print forest
            self.print_forest()
        print('Game ended. Thanks for playing.')

if __name__ == '__main__':
    g = Game()
    g.run()
