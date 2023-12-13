"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Class used to construct a wayland layer shell.
License           : GPL3
"""

from typing import Optional
from ..external_libraries import Gdk, Gtk, GtkLayerShell
from ..utils.layer_shell import Edges, Levels, Margins

class LayerShell:
    def __init__(
            self,
            namespace: str,
            monitor_id: Optional[int] = None,
            auto_exclusive_zone: Optional[bool] = None,
            exclusive_zone: Optional[int] = None,
            level: Optional[Levels] = None,
            anchor_edges: Optional[list[Edges]] = None,
            margins: Optional[Margins] = None
    ):
        self._window = Gtk.Window()
        self._namespace: str = namespace

        self._monitor_id: int = monitor_id if monitor_id is not None else 0
        self._auto_exclusive_zone: bool = auto_exclusive_zone if auto_exclusive_zone is not None else False
        self._exclusive_zone: int = exclusive_zone if exclusive_zone is not None else 0
        self._level: Levels = level if level is not None else Levels.BACKGROUND
        self._anchor_edges: list[Edges] = anchor_edges if anchor_edges is not None else [Edges.TOP, Edges.RIGHT, Edges.BOTTOM, Edges.LEFT]
        self._margins: Margins = margins if margins is not None else Margins({'top': 0, 'right': 0, 'bottom': 0, 'left': 0})

        GtkLayerShell.init_for_window(self._window)
        GtkLayerShell.set_namespace(self._window, self._namespace)
        self.set_monitor_id()
        self.set_auto_exclusive_zone()
        self.set_level()
        self.set_anchor_edges()
    
    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def monitor_id(self) -> int:
        return self._monitor_id
    
    def set_monitor_id(self, value: Optional[int] = None):
        if value != None: self._monitor_id = value

        GtkLayerShell.set_monitor(
            self._window,
            Gdk.Display.get_default().get_monitor(self._monitor_id)
        )

    @property
    def auto_exclusive_zone(self) -> bool:
        return self._auto_exclusive_zone
    
    def set_auto_exclusive_zone(self, value: Optional[bool] = None):
        if value != None: self._auto_exclusive_zone = value

        if self._auto_exclusive_zone:
            GtkLayerShell.auto_exclusive_zone_enable(self._window)
        else:
            GtkLayerShell.set_exclusive_zone(self._window, self._exclusive_zone)

    @property
    def exclusive_zone(self) -> int:
        return self._exclusive_zone
    
    def set_exclusive_zone(self, value: Optional[int] = None):
        if value != None: self._exclusive_zone = value
        self.auto_exclusive_zone = False
        GtkLayerShell.set_exclusive_zone(self._window, self._exclusive_zone)

    @property
    def level(self) -> Levels:
        return self._level.value
    
    def set_level(self, value: Optional[Levels] = None):
        if value != None: self._level = value
        GtkLayerShell.set_layer(self._window, self._level.value)

    @property
    def anchor_edges(self) -> list[Edges]:
        return self._anchor_edges
    
    def set_anchor_edges(self, value: Optional[list[Edges]] = None):
        if value != None: self._anchor_edges = value
        
        for edge in Edges:
            GtkLayerShell.set_anchor(self._window, edge.value, False)

        for edge in self._anchor_edges:
            GtkLayerShell.set_anchor(self._window, edge.value, True)

        self.set_margins()

    @property
    def margins(self) -> Margins:
        return self._margins
    
    def set_margins(self, value: Optional[Margins] = None):
        if value != None: self._margins = value

        GtkLayerShell.set_margin(self._window, Edges.TOP.value, self._margins.top)
        GtkLayerShell.set_margin(self._window, Edges.RIGHT.value, self._margins.right)
        GtkLayerShell.set_margin(self._window, Edges.BOTTOM.value, self._margins.bottom)
        GtkLayerShell.set_margin(self._window, Edges.LEFT.value, self._margins.left)