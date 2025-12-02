from event import Event
from player import Player

class Pond(Event):
    def __init__(self) -> None:
        self._drank = False

    # Implementation of the abstract encounter method override
    def encounter(self, player: Player) -> bool:
        if not self._drank:
            print('You drink from the pond.')
            player.drank()
            self._drank = True
        else:
            print("You're not thirsty.")
        # Pond stays in the forest (not removed)
        return False

    def symbol(self) -> str:
        return 'P'
