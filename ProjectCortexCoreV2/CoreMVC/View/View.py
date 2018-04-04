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

        ############################################################
        # Infrared Boundary
        ############################################################
        self.main_gui.horizontalslider_infrared_upper_boundary_hue.valueChanged['int'].connect(self.controller.set_infrared_upper_boundary_hue)
        self.main_gui.horizontalslider_infrared_upper_boundary_saturation.valueChanged['int'].connect(self.controller.set_infrared_upper_boundary_saturation)
        self.main_gui.horizontalslider_infrared_upper_boundary_value.valueChanged['int'].connect(self.controller.set_infrared_upper_boundary_value)
        self.main_gui.horizontalslider_infrared_lower_boundary_hue.valueChanged['int'].connect(self.controller.set_infrared_lower_boundary_hue)
        self.main_gui.horizontalslider_infrared_lower_boundary_saturation.valueChanged['int'].connect(self.controller.set_infrared_lower_boundary_saturation)
        self.main_gui.horizontalslider_infrared_lower_boundary_value.valueChanged['int'].connect(self.controller.set_infrared_lower_boundary_value)

        ############################################################
        # Morphological Transformation
        ############################################################
        self.main_gui.spinbox_infrared_blur_kernalsize.valueChanged['int'].connect(self.controller.set_blur_kernalsize)
        self.main_gui.spinbox_infrared_erode_iterations.valueChanged['int'].connect(self.controller.set_erode_iterations)
        self.main_gui.spinbox_infrared_dilate_iterations.valueChanged['int'].connect(self.controller.set_dilate_iterations)

    ############################################################
    # Preview RGB
    ############################################################
    def main_gui_set_label_rgb_camera_preview_frame(self, pixmap):
        self.main_gui.label_rgb_camera_preview.setPixmap(pixmap)

    def main_gui_clear_label_rgb_camera_preview_frame(self):
        self.main_gui.label_rgb_camera_preview.clear()

    ############################################################
    # Preview infrared
    ############################################################
    def main_gui_set_label_infrared_camera_preview_frame(self, pixmap):
        self.main_gui.label_infrared_camera_preview.setPixmap(pixmap)

    def main_gui_clear_label_infrared_camera_preview_frame(self):
        self.main_gui.label_infrared_camera_preview.clear()

    ############################################################
    # Serial
    ############################################################
    def get_combobox_serial_connection_port_current_text(self):
        if self.main_gui.combobox_serial_connection_ports.currentIndex() == -1:
            return None
        else:
            return self.main_gui.combobox_serial_connection_ports.currentText()

    def set_combobox_serial_connection_port_list(self, list):
        self.main_gui.combobox_serial_connection_ports.clear()
        self.main_gui.combobox_serial_connection_ports.addItems(list)

    def disable_button_refresh_combobox_serial_connection_ports(self):
        self.main_gui.button_refresh_combobox_serial_connection_ports.setEnabled(False)

    def disable_button_create_serial_connection(self):
        self.main_gui.button_create_serial_connection.setEnabled(False)

    ############################################################
    # Camera
    ############################################################
    def get_combobox_infrared_camera_index_current_text(self):
        if self.main_gui.combobox_infrared_camera_index.currentIndex() == -1:
            return None
        else:
            return self.main_gui.combobox_infrared_camera_index.currentText()

    def get_combobox_rgb_camera_index_current_text(self):
        if self.main_gui.combobox_rgb_camera_index.currentIndex() == -1:
            return None
        else:
            return self.main_gui.combobox_rgb_camera_index.currentText()

    def set_combobox_infrared_camera_index_list(self, list):
        self.main_gui.combobox_infrared_camera_index.clear()
        self.main_gui.combobox_infrared_camera_index.addItems(list)

    def set_combobox_rgb_camera_index_list(self, list):
        self.main_gui.combobox_rgb_camera_index.clear()
        self.main_gui.combobox_rgb_camera_index.addItems(list)

    def disable_button_refresh_combobox_camera_index(self):
        self.main_gui.button_refresh_combobox_camera_index.setEnabled(False)
        
    ############################################################
    # Record, Preview, Track
    ############################################################
    def disable_button_start_record(self):
        self.main_gui.button_start_record.setEnabled(False)

    def disable_button_stop_record(self):
        self.main_gui.button_stop_record.setEnabled(False)

    def disable_button_start_preview(self):
        self.main_gui.button_start_preview.setEnabled(False)

    def disable_button_stop_preview(self):
        self.main_gui.button_stop_preview.setEnabled(False)

    def disable_button_start_tracking(self):
        self.main_gui.button_start_tracking.setEnabled(False)

    def disable_button_stop_tracking(self):
        self.main_gui.button_stop_tracking.setEnabled(False)

    def enable_button_start_record(self):
        self.main_gui.button_start_record.setEnabled(True)

    def enable_button_stop_record(self):
        self.main_gui.button_stop_record.setEnabled(True)

    def enable_button_start_preview(self):
        self.main_gui.button_start_preview.setEnabled(True)

    def enable_button_stop_preview(self):
        self.main_gui.button_stop_preview.setEnabled(True)

    def enable_button_start_tracking(self):
        self.main_gui.button_start_tracking.setEnabled(True)

    def enable_button_stop_tracking(self):
        self.main_gui.button_stop_tracking.setEnabled(True)


    ############################################################
    # Infrared Boundary
    ############################################################
    def init_infrared_boundary_value(self, lower_boundary, upper_boundary):
        self.main_gui.horizontalslider_infrared_upper_boundary_hue.setValue(upper_boundary[0])
        self.main_gui.horizontalslider_infrared_upper_boundary_saturation.setValue(upper_boundary[1])
        self.main_gui.horizontalslider_infrared_upper_boundary_value.setValue(upper_boundary[2])
        self.main_gui.horizontalslider_infrared_lower_boundary_hue.setValue(lower_boundary[0])
        self.main_gui.horizontalslider_infrared_lower_boundary_saturation.setValue(lower_boundary[1])
        self.main_gui.horizontalslider_infrared_lower_boundary_value.setValue(lower_boundary[2])

    ############################################################
    # Morphological Transformation
    ############################################################
    def init_morphological_transformation_setup(self, blur_kernalsize, erode_iterations, dilate_iterations):
        self.main_gui.spinbox_infrared_blur_kernalsize.setValue(blur_kernalsize)
        self.main_gui.spinbox_infrared_erode_iterations.setValue(erode_iterations)
        self.main_gui.spinbox_infrared_dilate_iterations.setValue(dilate_iterations)
