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
        # Recording
        ############################################################
        self.main_gui.button_start_record.clicked.connect(self.controller.start_record)
        self.main_gui.button_stop_record.clicked.connect(self.controller.stop_record)

        ############################################################
        # Manual Control
        ############################################################

        ############################################################
        # Manual Control - Gimbal Control
        ############################################################

        self.main_gui.button_manual_gimbal_up.clicked.connect(self.controller.manual_gimbal_up)
        self.main_gui.button_manual_gimbal_down.clicked.connect(self.controller.manual_gimbal_down)
        self.main_gui.button_manual_gimbal_left.clicked.connect(self.controller.manual_gimbal_left)
        self.main_gui.button_manual_gimbal_right.clicked.connect(self.controller.manual_gimbal_right)

    def main_gui_set_label_videostream_frame(self, pixmap):
        self.main_gui.label_videostream.setPixmap(pixmap)

    def main_gui_clear_label_videostream_frame(self):
        self.main_gui.label_videostream.clear()
