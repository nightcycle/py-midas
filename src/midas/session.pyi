from .event import Event as Event, VersionData as VersionData, fill_down_event_from_previous as fill_down_event_from_previous, fill_down_events as fill_down_events
from .playfab import get_playfab_str_from_datetime as get_playfab_str_from_datetime
from _typeshed import Incomplete
from typing import TypedDict

class SessionDumpData(TypedDict):
    session_id: str
    user_id: str
    timestamp: str
    version: VersionData
    index: int
    event_count: int
    revenue: int
    duration: float

class Session:
    playfab_session_id: Incomplete
    session_id: Incomplete
    user_id: Incomplete
    events: Incomplete
    version: Incomplete
    is_studio: Incomplete
    timestamp: Incomplete
    version_text: Incomplete
    start_timestamp: Incomplete
    finish_timestamp: Incomplete
    duration: Incomplete
    revenue: int
    index: int
    def __init__(self, events: list[Event], session_id: str, playfab_session_id: str, user_id: str, version: VersionData, is_studio: bool, version_text: str) -> None: ...
    def __lt__(self, other): ...
    def dump(self) -> SessionDumpData: ...

def get_user_id(events: list[Event]) -> str | None: ...
def get_version(events: list[Event]) -> VersionData | None: ...
def get_is_studio(events: list[Event]) -> bool | None: ...
def get_version_text(events: list[Event]) -> str | None: ...
def safe_construct_session(session_id: str, playfab_session_id: str, session_event_list: list[Event]) -> Session | None: ...
def get_survival_rate(sessions: list[Session]) -> float: ...
def get_sessions_from_events(events: list[Event], fill_down_enabled: bool = ..., recursive_fill_down: bool = ...) -> list[Session]: ...
