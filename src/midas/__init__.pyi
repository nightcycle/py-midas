from event import Event, EventDumpData as EventDumpData
from pandas import DataFrame
from session import Session, SessionDumpData as SessionDumpData
from user import User, UserDumpData as UserDumpData

def dump(objects: list[Event] | list[Session] | list[User]): ...
def load(decoded_df: DataFrame) -> tuple[list[Event], list[Session], list[User]]: ...
