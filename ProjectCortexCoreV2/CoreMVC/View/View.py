from CoreMVC.View.MainGui import MainGui


class View():
    def __init__(self, app):
        self.app = app

    def set_controller(self, controller):
        self.controller = controller

    ############################################################
    # Main Gui
    ############################################################
    def main_gui_create(self):
        self.main_gui = MainGui(controller = self.controller)

    def main_gui_show(self):
        self.main_gui.show()

    def main_gui_setup_ui_slots(self):
        ############################################################
        # Preview
        ############################################################
        self.main_gui.button_start_preview.clicked.connect(self.controller.start_video_preview)
        self.main_gui.button_stop_preview.clicked.connect(self.controller.stop_video_preview)

        ############################################################
        # Tracking
        ############################################################
        self.main_gui.button_start_tracking.clicked.connect(self.controller.start_tracking)
        self.main_gui.button_stop_tracking.clicked.connect(self.controller.stop_tracking)

        ############################################################
        # Release Videostream (Deprecated)
        ############################################################
        self.main_gui.button_release_rgb_camera_videostream.setDisabled(True)
        self.main_gui.button_release_infrared_camera_videostream.setDisabled(True)

        ############################################################
        # Recording
        ############################################################
        self.main_gui.button_start_record.clicked.connect(self.controller.start_record)
        self.main_gui.button_stop_record.clicked.connect(self.controller.stop_record)

    def main_gui_set_label_videostream_frame(self, pixmap):
        self.main_gui.label_videostream.setPixmap(pixmap)
