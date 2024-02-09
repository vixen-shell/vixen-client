"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Class used to construct and display a wayland layer shell frame.
License           : GPL3

Additional Information:
- It would be wise to subsequently separate the creation and display functions.
"""

from .webView import webView
from .LayerShell import LayerShell
from .entities import LayerFrameSetting
from ..apiSocket import api_socket
from ..external_libraries import Gtk
from ..globals import frameCounter

class LayerFrame(LayerShell):
    def __init__(self, setting: LayerFrameSetting, dev: bool = False):
        super().__init__(
            setting.namespace,
            setting.monitor_id,
            setting.auto_exclusive_zone,
            setting.exclusive_zone,
            setting.level,
            setting.anchor_edges,
            setting.margins
        )

        self._window.add(
            webView(
                feature_name = setting.feature,
                width = setting.width,
                height = setting.height,
                layer_frame = True,
                dev = dev
            )
        )

        def on_destroy(window):
            frameCounter.decrement()
            if frameCounter.value == 0:
                api_socket.send({'id': 'close_client'})

        self._window.connect('destroy', on_destroy)
        self._window.show_all()