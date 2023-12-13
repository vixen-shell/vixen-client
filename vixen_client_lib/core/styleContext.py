"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Module for managing the Gtk css context.
License           : GPL3

Additional Information:
- Here we set the background of the window to be transparent.
"""

from ..external_libraries import Gdk, Gtk

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