from .setting import FrameSetting, LayerSetting
from .utils import build_frame_content, layerise_frame
from ...external_libraries import Gtk

class FrameView(Gtk.Window):
    def __init__(self, feature: str, route: str | None, is_layer: bool):
        Gtk.Window.__init__(self)
        self.set_app_paintable(True)
        build_frame_content(self, feature, route, is_layer)

def create_frame_view(feature: str, frame_setting: FrameSetting):
    is_layer = True if frame_setting.layer else False
    frame = FrameView(feature, frame_setting.route, is_layer)

    def layerise():
        frame.set_size_request(
            frame_setting.layer.width,
            frame_setting.layer.height
        )
        layerise_frame(frame, frame_setting.layer)

    def connect_events():
        if not is_layer:
            def on_delete_event(frame, event):
                frame.hide()
                return True
            
            frame.connect('delete-event', on_delete_event)

    if is_layer: layerise()
    connect_events()
    return frame

class _FrameView(Gtk.Window):
    def __init__(self, setting: FrameSetting):
        Gtk.Window.__init__(self)
        self.set_app_paintable(True)

        self.setting = setting
        self.is_layer = True if setting.layer else False

        build_frame_content(
            self,
            self.setting.feature,
            self.setting.route,
            self.is_layer
        )

        if self.is_layer:
            self.layerise()
        else:
            def on_delete_event(window, event):
                self.hide()
                return True

            self.connect('delete-event', on_delete_event)

        self.hide()

    def layerise(self):
        self.set_size_request(
            self.setting.layer.width,
            self.setting.layer.height
        )
        
        layerise_frame(self, self.setting.layer)