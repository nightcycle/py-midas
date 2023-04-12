from .event import Event as Event
from .playfab import get_playfab_str_from_datetime as get_playfab_str_from_datetime
from _typeshed import Incomplete
from copy import deepcopy as deepcopy
from datetime import datetime
from typing import TypedDict

class SessionDumpData(TypedDict):
    session_id: str
    user_id: str
    timestamp: str
    version_text: str
    index: int
    event_count: int
    revenue: int
    is_singular_version: bool
    duration: float

class Session:
    session_id: str
    user_id: str
    is_studio: bool
    events: list[Event]
    timestamp: datetime
    version_text: str
    is_singular_version: bool
    duration: Incomplete
    revenue: int
    index: int
    def __init__(self, events: list[Event]) -> None: ...
    def __lt__(self, other): ...
    def dump(self) -> SessionDumpData: ...

def get_survival_rate(sessions: list[Session]) -> float: ...
def get_sessions_from_events(events: list[Event], sessions_must_include_exit_and_enter_events: bool = ..., exit_event_name: str = ..., enter_event_name: str = ...) -> list[Session]: ...
