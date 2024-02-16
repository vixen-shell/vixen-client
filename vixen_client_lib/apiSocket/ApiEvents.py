from typing import Literal, TypedDict, Optional, Union

# Event Ids
ClientRuntimeEventIds = Literal['close_client']
FrameRuntimeEventIds = Literal['open_frame', 'close_frame']
EventIds = Literal[ClientRuntimeEventIds, FrameRuntimeEventIds]

# Event Data
class OpenFrameEventData(TypedDict):
    frame_name: str

class CloseFrameEventData(TypedDict):
    frame_name: str

class ApiEventObject(TypedDict):
    id: EventIds
    data: Optional[Union[
        OpenFrameEventData,
        CloseFrameEventData
    ]]