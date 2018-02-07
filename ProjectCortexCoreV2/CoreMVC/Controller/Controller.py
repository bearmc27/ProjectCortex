class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    ############################################################
    # Serial
    ############################################################
    def create_serial_connection(self):
        print("Create Serial Model")
        baudrate = 57600
        port = self.view.get_combobox_serial_connection_port_current_text()
        if port == -1:
            print("Serial Port Not Selected")
        else:
            self.model.create_serial_connection(baudrate=baudrate, port=port)

    def refresh_combobox_serial_connection_port(self):
        print("Refresh ComboBox Serial Connection Port")
        available_serial_ports = self.model.get_available_serial_ports_list()
        self.view.set_combobox_serial_connection_port_list(list=[row[0] for row in available_serial_ports])

    ############################################################
    # Preview
    ############################################################
    def start_video_preview(self):
        print("Start Video Preview")
        self.model.start_video_preview()

    def stop_video_preview(self):
        print("Stop Video Preview")
        self.model.stop_video_preview()

    def main_gui_set_label_videostream_frame(self, pixmap):
        self.view.main_gui_set_label_videostream_frame(pixmap=pixmap)

    def main_gui_clear_label_videostream_frame(self):
        self.view.main_gui_clear_label_videostream_frame()

    ############################################################
    # Tracking
    ############################################################
    def start_tracking(self):
        print("Start Video Tracking")
        # TODO: make sure serial model actually created and running
        self.model.start_tracking()

    def stop_tracking(self):
        print("Stop Video Tracking")
        self.model.stop_tracking()

    ############################################################
    # Recording
    ############################################################
    def start_record(self):
        print("Start Record")
        self.model.start_record()

    def stop_record(self):
        print("Stop Record")
        self.model.stop_record()

    ############################################################
    # Close Event
    ############################################################
    def main_gui_closeEvent(self):
        # Terminate all thread, if any
        self.model.main_gui_closeEvent()

    ############################################################
    # Manual Control
    ############################################################

    ############################################################
    # Manual Control - Gimbal Control
    ############################################################

    def manual_gimbal_up(self):
        print("Manual Gimbal Up")
        self.model.manual_gimbal_up()

    def manual_gimbal_down(self):
        print("Manual Gimbal Down")
        self.model.manual_gimbal_down()

    def manual_gimbal_left(self):
        print("Manual Gimbal Left")
        self.model.manual_gimbal_left()

    def manual_gimbal_right(self):
        print("Manual Gimbal Right")
        self.model.manual_gimbal_right()

    ############################################################
    # Camera Setup
    ############################################################
    def setup_infrared_camera(self):
        print("Setup Infrared Camera")
        index = self.view.get_combobox_infrared_camera_index_current_text()
        if index is None:
            print("Infrared Camera Index Not Selected")
        else:
            index = int(index)
            self.model.setup_infrared_camera(index=index)

            # TODO: Remove these code
            self.infrared_camera_set_resolution()

    def setup_rgb_camera(self):
        print("Setup RGB Camera")
        index = self.view.get_combobox_rgb_camera_index_current_text()
        if index is None:
            print("RGB Camera Index Not Selected")
        else:
            index = int(index)
            self.model.setup_rgb_camera(index=index)

            # TODO: Remove these code
            self.rgb_camera_set_resolution()

    def refresh_combobox_camera_index_list(self):
        print("Refresh Combobox Infrared Camera Index")
        available_camera_indexes = self.model.get_available_camera_index_list()
        self.view.set_combobox_infrared_camera_index_list(list=available_camera_indexes)
        self.view.set_combobox_rgb_camera_index_list(list=available_camera_indexes)

    def infrared_camera_set_resolution(self, width=640, height=360):
        print("Set Infrared Camera Resolution")
        self.model.infrared_camera_set_resolution(width=width, height=height)

    def rgb_camera_set_resolution(self, width=1280, height=720):
        print("Set RGB Camera Resolution")
        self.model.rgb_camera_set_resolution(width=width, height=height)

    ############################################################
    # Infrared Boundary
    ############################################################
    def set_infrared_upper_boundary_hue(self, hue):
        self.model.set_infrared_upper_boundary_hue(hue=hue)

    def set_infrared_upper_boundary_saturation(self, saturation):
        self.model.set_infrared_upper_boundary_saturation(saturation=saturation)

    def set_infrared_upper_boundary_value(self, value):
        self.model.set_infrared_upper_boundary_value(value=value)

    def set_infrared_lower_boundary_hue(self, hue):
        self.model.set_infrared_lower_boundary_hue(hue=hue)

    def set_infrared_lower_boundary_saturation(self, saturation):
        self.model.set_infrared_lower_boundary_saturation(saturation=saturation)

    def set_infrared_lower_boundary_value(self, value):
        self.model.set_infrared_lower_boundary_value(value=value)

    ############################################################
    # Morphological Transformation
    ############################################################
    def set_blur_kernalsize(self, blur_kernalsize):
        self.model.set_blur_kernalsize(blur_kernalsize=blur_kernalsize)

    def set_erode_iterations(self, erode_iterations):
        self.model.set_erode_iteration(erode_iterations=erode_iterations)

    def set_dilate_iterations(self, dilate_iterations):
        self.model.set_dilate_iteration(dilate_iterations=dilate_iterations)
