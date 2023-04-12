from _typeshed import Incomplete
from azure.kusto.data.exceptions import KustoServiceError as KustoServiceError
from copy import deepcopy as deepcopy
from datetime import datetime
from typing import TypedDict

CLUSTER: str
DEFAULT_QUERY: str
PLAYFAB_DATE_FORMAT: str
PLAYFAB_DATE_FORMAT_WITHOUT_FRACTION: str
PLAYFAB_DATE_FORMAT_WITH_FRACTION_NO_TZ: str

class UserData(TypedDict):
    PlayFabUserId: str
    EventCount: int
    JoinTimestamp: str

class RawRowData(TypedDict):
    EventData: str
    Timestamp: str
    PlayFabUserId: str
    EventName: str
    EventId: str

def get_datetime_from_playfab_str(playfab_str: str) -> datetime: ...
def get_playfab_str_from_datetime(datetime: datetime) -> str: ...
def update_based_on_success(is_success: bool, event_limit: int, fail_delay: int, original_list_limit: int, event_update_increment: int, delay_update_increment: int): ...

class PlayFabClient:
    title_id: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    tenant_id: Incomplete
    client: Incomplete
    def __init__(self, client_id=..., client_secret=..., tenant_id=..., title_id=...) -> None: ...
    def query(self, query=...): ...
    def query_user_data_list(self, user_join_floor: datetime, join_window_in_days: int, user_limit: int = ...) -> list[UserData]: ...
    def query_events_from_user_data(self, playfab_user_ids: list[str], user_join_floor: datetime) -> list[RawRowData]: ...
    def recursively_query_events(self, user_data_list: list[UserData], event_limit: int, fail_delay: int, original_list_limit: int, event_update_increment: int, delay_update_increment: int, user_join_floor: datetime, start_tick: float, total_events: int, completed_events: int = ..., start_index: int = ...) -> list[RawRowData]: ...
    def download_all_event_data(self, user_join_floor: str | datetime, join_window_in_days: int, user_limit: int = ..., max_event_list_length: int = ..., update_increment: int = ...) -> list[RawRowData]: ...
