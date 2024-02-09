"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Layer shell entities.
License           : GPL3
"""

from enum import Enum
from ...external_libraries import GtkLayerShell

class Levels(Enum):
    BACKGROUND = GtkLayerShell.Layer.BACKGROUND
    BOTTOM = GtkLayerShell.Layer.BOTTOM
    TOP = GtkLayerShell.Layer.TOP
    OVERLAY = GtkLayerShell.Layer.OVERLAY

class Edges(Enum):
    TOP = GtkLayerShell.Edge.TOP
    RIGHT = GtkLayerShell.Edge.RIGHT
    BOTTOM = GtkLayerShell.Edge.BOTTOM
    LEFT = GtkLayerShell.Edge.LEFT

class Margins:
    def __init__(self, margins: dict):
        self._margins = margins

        valid_keys = ['top', 'right', 'bottom', 'left']

        for key in valid_keys:
            if key not in self._margins: self._margins[key] = 0

        self.top: int = self._margins['top']
        self.right: int = self._margins['right']
        self.bottom: int = self._margins['bottom']
        self.left: int = self._margins['left']