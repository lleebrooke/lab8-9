from event import Event
from player import Player

class BlueberryBush(Event):
    # Implementation of the abstract encounter method override
    def encounter(self, player: Player) -> bool:
        print('You chow down on some tasty blueberries.')
        player.eat()
        # Return True to indicate the bush should be removed after encounter
        return True

    def symbol(self) -> str:
        return 'B'
