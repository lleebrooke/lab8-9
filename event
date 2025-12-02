from event import Event
from player import Player

class DeerHerd(Event):
    # Implementation of the abstract encounter method override
    def encounter(self, player: Player) -> bool:
        # If player has drunk and eaten both bushes, they win.
        if player.has_drank() and player.blueberries_eaten() >= 2:
            print("You've finished browsing for the day and arrived safely back at the herd.")
            # Returning False (no removal) but caller will end the game on this message.
            return False
        # Otherwise nothing happens.
        return False

    def symbol(self) -> str:
        return 'H'
