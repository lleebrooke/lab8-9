from typing import Optional
from event import Event

class ForestPatch:
    def __init__(self) -> None:
        self._event: Optional[Event] = None

    def set_event(self, event: Optional[Event]) -> None:
        self._event = event

    def get_event(self) -> Optional[Event]:
        return self._event

    def remove_event(self) -> None:
        self._event = None

    def symbol(self) -> str:
        if self._event is None:
            return ' '
        return self._event.symbol()
