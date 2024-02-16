"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : vixen display client library.
License           : GPL3
"""

import os, json
os.environ['GDK_BACKEND'] = 'wayland'

from typing import Dict
from .constants import API_URI
from .core import ClientSetting, frame_handler
from .apiSocket import api_socket, check_port, ApiEventObject
from .external_libraries import Gtk

class ClientStarter:
    def start(self, feature_name: str, client_id: str):
        if not check_port(API_URI.host, API_URI.port):
            raise Exception('Vixen Api is not running!')
            
        api_socket.run(client_id)

        file_setting = f'{os.path.expanduser("~")}/.config/vixen/{feature_name}.json'
        with open(file_setting, 'r') as file:
            client_data_setting = json.load(file)
            file.close()

        frame_handler.set(ClientSetting(client_data_setting))
        Gtk.main()