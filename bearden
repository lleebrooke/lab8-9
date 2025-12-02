from event import Event
from player import Player

class BearDen(Event):
    def __init__(self) -> None:
        self._encounters = 0

    # Implementation of the abstract encounter method override
    def encounter(self, player: Player) -> bool:
        self._encounters += 1
        if self._encounters == 1:
            # Move player back: the caller will manage the player position; here we inform via printed message
            print("Whew, that was close! You almost woke a nearby bear.")
            # Return False (do not remove the den)
            return False
        else:
            print("You woke a nearby bear. It's hungry. Game over.")
            # Game-ending encounter; den remains.
            return False

    def symbol(self) -> str:
        # BearDens are hidden in display; represent as ' ' (space)
        return ' '
