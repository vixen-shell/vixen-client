"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : vixen display client library.
License           : GPL3
"""

import os, json
os.environ['GDK_BACKEND'] = 'wayland'

from .core import LayerFrame
from .core import WindowFrame
from .core import ClientSetting
from .apiSocket import api_socket, check_port
from .external_libraries import Gtk
from .globals import frameCounter
from .constants import API_URI

class ClientStarter:
    def start(self, feature_name: str, client_id: str, dev: bool = False):
        if check_port(API_URI.host, API_URI.port):
            api_socket.run(client_id)
        else:
            raise Exception('Vixen Api is not running!')
        
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