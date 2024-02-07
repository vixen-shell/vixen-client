"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Class used to start a display client.
License           : GPL3
"""

import os
os.environ['GDK_BACKEND'] = 'wayland'

import json
from .ApiSocket import api_socket
from .LayerFrame import LayerFrame
from .WindowFrame import WindowFrame
from ..external_libraries import Gtk
from ..utils.setting import ClientSetting
from ..utils.globals import frameCounter

import time

class ClientStarter:
    def __init__(self, client_id: str) -> None:
        self.client_id = client_id
        api_socket.run(client_id)
        
    def start(self, feature_name: str, dev: bool = False):
        self._frame_list = []

        file_setting = f'{os.path.expanduser("~")}/.config/vixen/{feature_name}.json'
        with open(file_setting, 'r') as file:
            data_setting = json.load(file)
            file.close()
        
        self._client_setting = ClientSetting(data_setting)

        frame = {
            'layer': LayerFrame,
            'window': WindowFrame
        }

        for frame_setting in self._client_setting.frame_setting_list:
            self._frame_list.append(frame[frame_setting.mode](frame_setting, dev))
            frameCounter.increment()

        Gtk.main()

    def stop(self):
        Gtk.main_quit()