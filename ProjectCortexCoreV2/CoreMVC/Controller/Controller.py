class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    ############################################################
    # View
    ############################################################
    def start_video_preview(self):
        print("Start Video Preview")
        self.model.create_rgb_camera()
        self.model.create_rgb_camera_videostream(camera_index = 2)
        self.model.start_video_preview()

    def stop_video_preview(self):
        print("Stop Video Preview")
        self.model.rgb_camera_stop_videostream()
        self.model.stop_video_preview()

    def start_tracking(self):
        print("Start Video Tracking")
        self.model.create_serial_model(57600, "COM6")
        self.model.create_infrared_camera()
        self.model.create_infrared_camera_videostream(camera_index = 0)
        self.model.start_tracking()

    def stop_tracking(self):
        print("Stop Video Tracking")
        self.model.infrared_camera_stop_videostream()
        self.model.stop_tracking()

    def main_gui_closeEvent(self):
        # Terminate all thread, if any
        self.model.infrared_camera_stop_videostream()
        self.model.rgb_camera_stop_videostream()
        self.model.stop_video_preview()
        self.model.stop_tracking()

    ############################################################
    # Model
    ############################################################
    def infrared_camera_get_frame(self):
        return self.model.infrared_camera_get_frame()
