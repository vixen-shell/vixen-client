from typing import Dict
from .ClientSetting import ClientSetting
from .frame_view import create_frame_view, FrameView
from ..apiSocket import api_socket, ApiEventObject
from ..external_libraries import GLib

class FrameHandler:
    def __init__(self) -> None:
        self._is_set: bool = False

    def _connect_api_events(self):
        def open_frame(event: ApiEventObject):
            if event['id'] == 'open_frame':
                self._frames[event['data']['frame_name']].show_all()

        def close_frame(event: ApiEventObject):
            if event['id'] == 'close_frame':
                self._frames[event['data']['frame_name']].hide()

        api_socket.add_listener(open_frame)
        api_socket.add_listener(close_frame)

    def set(self, client_setting: ClientSetting):
        self._client_setting = client_setting.get_client_setting
        self._frame_settings = client_setting.get_frame_settings
        self._frames: Dict[str, FrameView] = {}

        def add_frame_after_main():
            for frame_name in self._frame_settings:
                self._frames[frame_name] = create_frame_view(
                    feature = self._client_setting.feature,
                    frame_setting = self._frame_settings[frame_name]
                )

            self._connect_api_events()

        GLib.idle_add(add_frame_after_main)
        self._is_set = True
    

frame_handler = FrameHandler()