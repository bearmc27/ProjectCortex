class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    ############################################################
    # Serial
    ############################################################
    def create_serial_model(self):
        print("Create Serial Model")
        self.model.create_serial_model(baudrate = 57600, port = "COM7")

    ############################################################
    # Preview
    ############################################################
    def start_video_preview(self):
        print("Start Video Preview")
        self.model.start_video_preview()

    def stop_video_preview(self):
        print("Stop Video Preview")
        self.model.stop_video_preview()

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
