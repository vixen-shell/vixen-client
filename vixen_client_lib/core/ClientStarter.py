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
# from .styleContext import init_style_context
from .LayerFrame import LayerFrame
from .WindowFrame import WindowFrame
from ..external_libraries import Gtk
from ..utils.setting import ClientSetting
from ..utils.globals import frameCounter

class ClientStarter:
    def start(self, file_setting: str, dev: bool = False):
        self._frame_list = []

        with open(file_setting, 'r') as file:
            data_setting = json.load(file)
        
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