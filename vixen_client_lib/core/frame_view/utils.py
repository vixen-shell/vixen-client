"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Module for creating a Gtk webview.
License           : GPL3
"""

from ..layerise import layerise_window
from .setting import LayerSetting
from ...external_libraries import Gtk, Gdk, WebKit2
from ...constants import FRONT_URI

def build_frame_content(
        frame: Gtk.Window,
        feature: str,
        route: str | None = None, 
        layer: bool = False
):
    def webView():
        def init_style_context():
            stylesheet = b"""
            window {
                background-color: transparent;
            }
            """
            style_provider = Gtk.CssProvider()
            style_provider.load_from_data(stylesheet)
            Gtk.StyleContext.add_provider_for_screen(
                Gdk.Screen.get_default(),
                style_provider,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
            )

        def webKit_settings():
            settings = WebKit2.Settings()
            settings.set_property("hardware_acceleration_policy", WebKit2.HardwareAccelerationPolicy.ALWAYS)
            settings.set_property("enable-developer-extras", True)
            return settings

        webview = WebKit2.WebView()
        webview.set_settings(webKit_settings())

        if layer:
            init_style_context()
            webview.set_background_color(
                Gdk.RGBA(red=0, green=0, blue=0, alpha=0.0)
            )

        route_param = f'&route={route}' if route else ''
        webview.load_uri(f"{FRONT_URI.http}/?feature={feature}{route_param}")

        return webview
    
    frame.add(webView())

def layerise_frame(frame: Gtk.Window, layer_setting: LayerSetting):
    layerise_window(
        frame,
        layer_setting.namespace,
        layer_setting.monitor_id,
        layer_setting.auto_exclusive_zone,
        layer_setting.exclusive_zone,
        layer_setting.level,
        layer_setting.anchor_edges,
        layer_setting.margins
    )