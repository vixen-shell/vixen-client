from typing import Dict
from .frame_view import FrameSetting

class ClientDataSetting:
    def __init__(self, feature: str, single_instance: bool):
        self.feature: str = feature
        self.single_instance: bool = single_instance

class ClientSetting:
    def __init__(self, data: dict):
        self._feature: str = data['feature']
        self._single_instance: bool = data.get('single_instance') or False
        self._frame_settings: Dict[str, FrameSetting] = {}

        for frame_data in data['frames']:
            self._frame_settings[frame_data['name']] = FrameSetting(self._feature, frame_data)

    @property
    def get_client_setting(self) -> ClientDataSetting:
        return ClientDataSetting(
            self._feature,
            self._single_instance
        )
    
    @property
    def get_frame_settings(self) -> Dict[str, FrameSetting]:
        return self._frame_settings