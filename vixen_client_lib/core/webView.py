"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Module for creating a Gtk webview.
License           : GPL3
"""

from ..external_libraries import Gdk, WebKit2

def webKit_settings():
    settings = WebKit2.Settings()
    settings.set_property("hardware_acceleration_policy", WebKit2.HardwareAccelerationPolicy.ALWAYS)
    settings.set_property("enable-developer-extras", True)
    return settings

def webView(url: str, width: int, height: int):
    webview = WebKit2.WebView()
    webview.set_settings(webKit_settings())

    webview.set_background_color(
        Gdk.RGBA(
            red=0,
            green=0,
            blue=0,
            alpha=0.0,
        )
    )

    webview.load_uri(url)
    webview.set_size_request(width, height)

    return webview