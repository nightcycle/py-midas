from _typeshed import Incomplete
from data_encoder import BaseStateTree as BaseStateTree, DecodedRowData as RowData, EventData as EventData, IdentificationData as IdentificationData, IndexData as IndexData, VersionData as VersionData
from datetime import datetime
from pandas import DataFrame as DataFrame
from typing import Any

def version_to_version_text(version: VersionData, is_hotfix_included: bool = ..., is_tag_included: bool = ..., is_test_group_included: bool = ..., is_build_included: bool = ...): ...

class EventDumpData:
    state_data: BaseStateTree
    name: str
    timestamp: str
    event_id: str
    version_text: str
    index: int
    first_event_found: bool
    is_sequential: bool

class Event:
    name: str
    playfab_session_id: str
    event_id: str
    timestamp: datetime
    version_text: str
    session_id: str | None
    user_id: str | None
    place_id: str | None
    version: VersionData
    index: int
    is_studio: bool
    first_event_found: bool
    is_sequential: bool
    state_data: Incomplete
    def __init__(self, row_data: RowData) -> None: ...
    def __lt__(self, other): ...
    def dump(self) -> EventDumpData: ...

def fill_down(current_data: dict | None, prev_data: dict | None): ...
def transfer_property(previous_data: dict, current_data: dict): ...
def fill_down_event_from_previous(previous: Event, current: Event): ...
def fill_down_events(session_events: list[Event], current: Event, targetIndex: int, depth: int): ...
def flatten_table(all_event_data: dict[str, dict], column_prefix: str, row_data: dict): ...
def get_cell(table_data: dict[str, list[Any]], column_name: str, row_index: int): ...
def get_event_data_at_row(table_data: dict[str, list[Any]], row_index: int) -> EventData: ...
def get_events_from_df(decoded_df: DataFrame) -> list[Event]: ...
