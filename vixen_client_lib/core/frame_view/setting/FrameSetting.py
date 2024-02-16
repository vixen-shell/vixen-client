from .LayerSetting import LayerSetting

class FrameSetting:
    def __init__(self, feature: str, frame_data: dict):
        self.feature = feature
        self.route = frame_data.get('route')
        self.name = frame_data['name']
        self.title = frame_data['title']

        layer_data = frame_data.get('layer')
        self.layer = LayerSetting(self.title, layer_data) if layer_data else None