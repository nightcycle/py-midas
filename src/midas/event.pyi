from .data_encoder import BaseStateTree as BaseStateTree, DecodedRowData as RowData, EventData as EventData, VersionData as VersionData
from .playfab import get_datetime_from_playfab_str as get_datetime_from_playfab_str, get_playfab_str_from_datetime as get_playfab_str_from_datetime
from datetime import datetime
from pandas import DataFrame as DataFrame

SID_GEN_REFIX: str

def version_to_version_text(version: VersionData, is_hotfix_included: bool = ..., is_tag_included: bool = ..., is_test_group_included: bool = ..., is_build_included: bool = ...): ...

class EventDumpData:
    name: str
    event_id: str
    timestamp: str
    seconds_since_session_start: float
    version_text: str
    revenue: int
    session_id: str
    user_id: str
    place_id: str
    version: VersionData
    index: int
    is_studio: bool
    is_sequential: bool
    state_data: BaseStateTree

class Event:
    name: str
    event_id: str
    timestamp: datetime
    seconds_since_session_start: float
    version_text: str
    revenue: int
    session_id: str
    user_id: str
    place_id: str
    version: VersionData
    index: int
    is_studio: bool
    is_sequential: bool
    state_data: BaseStateTree
    def __init__(self, row_data: RowData) -> None: ...
    def __lt__(self, other): ...
    def dump(self) -> EventDumpData: ...

def get_events_from_df(decoded_df: DataFrame) -> list[Event]: ...
