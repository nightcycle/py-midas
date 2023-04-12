from .event import Event
from .session import Session, SessionDumpData as SessionDumpData
from .user import User, UserDumpData as UserDumpData
from pandas import DataFrame

def dump(objects: list[Event] | list[Session] | list[User]): ...
def load(decoded_df: DataFrame, stitch_session_separation_limit_seconds: int = ..., exit_event_name: str = ..., enter_event_name: str = ..., rejoin_event_name: str = ..., teleport_event_name: str = ..., sessions_must_include_exit_and_enter_events: bool = ..., fill_down_enabled: bool = ..., recursive_fill_down_enabled: bool = ...) -> tuple[list[Event], list[Session], list[User]]: ...
