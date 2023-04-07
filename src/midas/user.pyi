from _typeshed import Incomplete
from datetime import datetime
from session import Session as Session
from typing import TypedDict

class UserDumpData(TypedDict):
    user_id: str
    timestamp: str
    index: int
    session_count: int
    revenue: int
    duration: float
    is_retained_on_day: list[bool]

class User:
    user_id: str
    timestamp: datetime
    index: int
    session_count: int
    revenue: int
    duration: float
    is_retained_on_day: list[bool]
    sessions: Incomplete
    first_session_timestamp: Incomplete
    last_session_timestamp: Incomplete
    def __init__(self, sessions: list[Session]) -> None: ...
    def __lt__(self, other): ...
    def dump(self): ...

def get_users_from_session_list(sessions: list[Session]): ...
