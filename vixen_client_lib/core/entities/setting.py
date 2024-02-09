"""
Author            : Nohavye
Author's Email    : noha.poncelet@gmail.com
Repository        : https://github.com/vixen-shell/vixen-client.git
Description       : Setting entities.
License           : GPL3
"""

from typing import Optional
from .layerShell import Edges, Levels, Margins
from ...external_libraries import GtkLayerShell

class LayerFrameSetting:
    def __init__(self, data: dict):
        anchor_values = {
            'top': [Edges.TOP, Edges.LEFT, Edges.RIGHT],
            'right': [Edges.RIGHT, Edges.TOP, Edges.BOTTOM],
            'bottom': [Edges.BOTTOM, Edges.LEFT, Edges.RIGHT],
            'left': [Edges.LEFT, Edges.TOP, Edges.BOTTOM],

            'top left': [Edges.TOP, Edges.LEFT],
            'top right': [Edges.TOP, Edges.RIGHT],
            'bottom right': [Edges.BOTTOM, Edges.RIGHT],
            'bottom left': [Edges.BOTTOM, Edges.LEFT],

            'full': [Edges.TOP, Edges.RIGHT, Edges.BOTTOM, Edges.LEFT],
            'free': None
        }

        level_values = {
            'top': Levels.TOP,
            'bottom': Levels.BOTTOM,
            'overlay': Levels.OVERLAY,
            'background': Levels.BACKGROUND
        }

        self.mode: str = data['mode']
        self.feature: str = data['feature']
        self.namespace: str = data['namespace']
        self.monitor_id: Optional[int] = data['monitor_id'] if 'monitor_id' in data else None
        self.auto_exclusive_zone: Optional[bool] = data['auto_exclusive_zone'] if 'auto_exclusive_zone' in data else None
        self.exclusive_zone: Optional[int] = data['exclusive_zone'] if 'exclusive_zone' in data else None
        self.level: Optional[Levels] = level_values[data['level']] if 'level' in data else None
        self.anchor_edges: Optional[list[Edges]] = anchor_values[data['anchor_edges']] if 'anchor_edges' in data else None
        self.margins: Optional[Margins] = Margins(data['margins']) if 'margins' in data else None
        self.width: int = data['width'] if 'width' in data else -1
        self.height: int = data['height'] if 'height' in data else -1

class WindowFrameSetting:
    def __init__(self, data: dict):
        self.mode: str = data['mode']
        self.feature: str = data['feature']
        self.title: str = data['title']

class ClientSetting:
    def __init__(self, data: dict):
        self.frame_setting_list = []

        frame_setting = {
            'layer': LayerFrameSetting,
            'window': WindowFrameSetting
        }

        for frame_data in data['frames']:
            self.frame_setting_list.append(
                frame_setting[frame_data['mode']](frame_data)
            )