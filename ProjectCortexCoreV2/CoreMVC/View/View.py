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
        # Serial
        ############################################################
        self.main_gui.button_create_serial_connection.clicked.connect(self.controller.create_serial_connection)
        self.main_gui.button_refresh_combobox_serial_connection_ports.clicked.connect(self.controller.refresh_combobox_serial_connection_port)

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

        ############################################################
        # Camera Setup
        ############################################################
        self.main_gui.button_setup_infrared_camera.clicked.connect(self.controller.setup_infrared_camera)
        self.main_gui.button_setup_rgb_camera.clicked.connect(self.controller.setup_rgb_camera)
        self.main_gui.button_refresh_combobox_camera_index.clicked.connect(self.controller.refresh_combobox_camera_index_list)

        # ############################################################
        # # Testing
        # ############################################################
        # self.main_gui.verticalslider_infrared_upper_boundary_hue.valueChanged.connect(self.update_lcd_number_value)

    ############################################################
    # Preview
    ############################################################
    def main_gui_set_label_videostream_frame(self, pixmap):
        self.main_gui.label_videostream.setPixmap(pixmap)

    def main_gui_clear_label_videostream_frame(self):
        self.main_gui.label_videostream.clear()

    ############################################################
    # Serial
    ############################################################
    def get_combobox_serial_connection_port_current_text(self):
        return self.main_gui.combobox_serial_connection_ports.currentText()

    def set_combobox_serial_connection_port_list(self, list):
        self.main_gui.combobox_serial_connection_ports.clear()
        self.main_gui.combobox_serial_connection_ports.addItems(list)

    ############################################################
    # Camera
    ############################################################
    def get_combobox_infrared_camera_index_current_text(self):
        return self.main_gui.combobox_infrared_camera_index.currentText()

    def get_combobox_rgb_camera_index_current_text(self):
        return self.main_gui.combobox_rgb_camera_index.currentText()

    def set_combobox_infrared_camera_index_list(self, list):
        self.main_gui.combobox_infrared_camera_index.clear()
        self.main_gui.combobox_infrared_camera_index.addItems(list)

    def set_combobox_rgb_camera_index_list(self, list):
        self.main_gui.combobox_rgb_camera_index.clear()
        self.main_gui.combobox_rgb_camera_index.addItems(list)

    # ############################################################
    # # Testing
    # ############################################################
    # def update_lcd_number_value(self):
    #     self.main_gui.lcdnumber.display(self.main_gui.verticalslider_infrared_upper_boundary_hue.value())
