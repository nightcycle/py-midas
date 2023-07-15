from .event import Event as Event
from .playfab import get_playfab_str_from_datetime as get_playfab_str_from_datetime
from _typeshed import Incomplete
from datetime import datetime
from typing import Optional, TypedDict

ScreenRatio: Incomplete

class SessionDumpData(TypedDict):
    session_id: str
    user_id: str
    is_studio: bool
    timestamp: str
    version_text: str
    duration: float
    revenue: int
    index: int
    event_count: int
    account_age: Optional[int]
    roblox_language: Optional[str]
    system_language: Optional[str]
    accelerometer: Optional[bool]
    gamepad_enabled: Optional[bool]
    gyroscope_enabled: Optional[bool]
    keyboard_enabled: Optional[bool]
    mouse_enabled: Optional[bool]
    touch_enabled: Optional[bool]
    screen_size: Optional[int]
    screen_ratio: Optional[ScreenRatio]
    starting_group_memberships: Optional[dict[str, bool]]
    starting_gamepasses: Optional[dict[str, bool]]

class Session:
    session_id: str
    user_id: str
    events: list[Event]
    timestamp: datetime
    version_text: str
    duration: float
    revenue: int
    index: int
    is_studio: bool
    account_age: Optional[int]
    roblox_language: Optional[str]
    system_language: Optional[str]
    accelerometer: Optional[bool]
    gamepad_enabled: Optional[bool]
    gyroscope_enabled: Optional[bool]
    keyboard_enabled: Optional[bool]
    mouse_enabled: Optional[bool]
    touch_enabled: Optional[bool]
    screen_size: Optional[int]
    screen_ratio: Optional[ScreenRatio]
    starting_group_memberships: Optional[dict[str, bool]]
    starting_gamepasses: Optional[dict[str, bool]]
    def __init__(self, events: list[Event]) -> None: ...
    def __lt__(self, other): ...
    def dump(self) -> SessionDumpData: ...

def get_sessions_from_events(events: list[Event], sessions_must_include_exit_and_enter_events: bool = ..., exit_event_name: str = ..., enter_event_name: str = ...) -> list[Session]: ...
