from .event import Event
from .session import Session, SessionDumpData as SessionDumpData
from .user import User, UserDumpData as UserDumpData
from pandas import DataFrame

def dump(objects: list[Event] | list[Session] | list[User]): ...
def load(decoded_df: DataFrame) -> tuple[list[Event], list[Session], list[User]]: ...
