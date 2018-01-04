class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    ############################################################
    # View
    ############################################################

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
        self.model.create_serial_model(57600, "COM9")
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
