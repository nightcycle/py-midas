from .data_encoder import BaseStateTree as BaseStateTree, DecodedRowData as RowData, EventData as EventData, VersionData as VersionData
from .playfab import get_datetime_from_playfab_str as get_datetime_from_playfab_str, get_playfab_str_from_datetime as get_playfab_str_from_datetime
from _typeshed import Incomplete
from datetime import datetime
from pandas import DataFrame as DataFrame

SID_GEN_REFIX: str

def get_if_session_id_generated(session_id: str) -> bool: ...
def version_to_version_text(version: VersionData, is_hotfix_included: bool = ..., is_tag_included: bool = ..., is_test_group_included: bool = ..., is_build_included: bool = ...): ...

class EventDumpData:
    state_data: BaseStateTree
    name: str
    timestamp: str
    event_id: str
    session_id: str | None
    user_id: str
    version_text: str
    index: int
    first_event_found: bool
    is_sequential: bool

class Event:
    name: str
    event_id: str
    timestamp: datetime
    seconds_since_previous_event: None | float
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
    state_data: Incomplete
    def __init__(self, row_data: RowData) -> None: ...
    def __lt__(self, other): ...
    def dump(self) -> EventDumpData: ...

def fill_down(current_data: dict | None, prev_data: dict | None): ...
def transfer_property(previous_data: dict, current_data: dict): ...
def fill_down_event_from_previous(previous: Event, current: Event): ...
def fill_down_events(session_events: list[Event], current: Event, targetIndex: int, depth: int): ...
def get_events_from_df(decoded_df: DataFrame, stitch_session_separation_limit_seconds: int = ..., exit_event_name: str = ..., enter_event_name: str = ..., rejoin_event_name: str = ..., teleport_event_name: str = ..., fill_down_enabled: bool = ..., recursive_fill_down_enabled: bool = ...) -> list[Event]: ...
