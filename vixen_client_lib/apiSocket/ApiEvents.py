from typing import Literal, TypedDict, Optional, Union

# Event Ids
RuntimeEventIds = Literal['close_client']
EventIds = Literal[RuntimeEventIds]

# Event Data
class EventDataExampleA(TypedDict):
    data_a: str
    data_b: bool

class EventDataExampleB(TypedDict):
    data_c: str
    data_d: bool

class ApiEventObject(TypedDict):
    id: EventIds
    data: Optional[Union[
        EventDataExampleA,
        EventDataExampleB
    ]]