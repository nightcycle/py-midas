from .event import Event
from .session import Session, SessionDumpData as SessionDumpData
from .user import User, UserDumpData as UserDumpData
from pandas import DataFrame

def dump(objects: list[Event] | list[Session] | list[User]): ...
def load(decoded_df: DataFrame, exit_event_name: str = ..., enter_event_name: str = ..., sessions_must_include_exit_and_enter_events: bool = ...) -> tuple[list[Event], list[Session], list[User]]: ...
