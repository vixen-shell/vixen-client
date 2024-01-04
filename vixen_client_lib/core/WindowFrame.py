"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Class used to construct and display a window frame.
License           : GPL3

Additional Information:
- It would be wise to subsequently separate the creation and display functions.
"""

from .webView import webView
from ..external_libraries import Gtk
from ..utils.setting import WindowFrameSetting

class WindowFrame:
    def __init__(self, setting: WindowFrameSetting, dev: bool = False):
        self._window = Gtk.Window()
        self._window.set_title(setting.title)

        self._window.add(
            webView(
                frame_name = setting.name,
                width = -1,
                height = -1,
                dev = dev
            )
        )

        self._window.connect('destroy', Gtk.main_quit)
        self._window.show_all()