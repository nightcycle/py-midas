from .playfab import get_playfab_str_from_datetime as get_playfab_str_from_datetime
from .session import Session as Session
from _typeshed import Incomplete
from datetime import datetime
from typing import TypedDict

class UserDumpData(TypedDict):
    user_id: str
    timestamp: str
    index: int
    session_count: int
    net_revenue: int
    net_duration: float
    is_retained_on_d0: bool
    is_retained_on_d1: bool
    is_retained_on_d7: bool
    is_retained_on_d14: bool
    is_retained_on_d28: bool

class User:
    user_id: str
    timestamp: datetime
    index: int
    session_count: int
    net_revenue: int
    net_duration: float
    is_retained_on_d0: bool
    is_retained_on_d1: bool
    is_retained_on_d7: bool
    is_retained_on_d14: bool
    is_retained_on_d28: bool
    sessions: Incomplete
    def __init__(self, sessions: list[Session]) -> None: ...
    def __lt__(self, other): ...
    def dump(self) -> UserDumpData: ...

def get_users_from_session_list(sessions: list[Session]): ...
