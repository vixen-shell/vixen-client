"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Module for creating a Gtk webview.
License           : GPL3
"""

from .styleContext import init_style_context
from ..external_libraries import Gdk, WebKit2
from ..utils.constants import FRONT_URL, mode

def webKit_settings():
    settings = WebKit2.Settings()
    settings.set_property("hardware_acceleration_policy", WebKit2.HardwareAccelerationPolicy.ALWAYS)
    settings.set_property("enable-developer-extras", True)
    return settings

def webView(
    frame_name: str,
    width: int,
    height: int,
    layer_frame: bool = False,
    dev: bool = False
):
    webview = WebKit2.WebView()
    webview.set_settings(webKit_settings())

    if layer_frame:
        init_style_context()
        webview.set_background_color(
            Gdk.RGBA(red=0, green=0, blue=0, alpha=0.0)
        )

    webview.load_uri(f"{FRONT_URL[mode(dev)]}/?frame={frame_name}")
    webview.set_size_request(width, height)

    return webview