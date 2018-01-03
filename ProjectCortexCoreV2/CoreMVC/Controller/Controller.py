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
        self.model.create_rgb_camera_videostream(camera_index = 2)
        self.model.start_video_preview()

    def stop_video_preview(self):
        print("Stop Video Preview")
        self.model.rgb_camera_stop_videostream()
        self.model.stop_video_preview()

    ############################################################
    # Tracking
    ############################################################
    def start_tracking(self):
        print("Start Video Tracking")
        # TODO: make sure serial model actually created and running
        # self.model.create_serial_model(57600, "COM8")
        self.model.create_infrared_camera_videostream(camera_index = 1)
        self.model.start_tracking()

    def stop_tracking(self):
        print("Stop Video Tracking")
        self.model.infrared_camera_stop_videostream()
        self.model.stop_tracking()

    ############################################################
    # Release Videostream
    ############################################################
    def release_rgb_camera_videostream(self):
        print("Release RGB Camera Videostream")
        self.model.release_rgb_camera_videostream()

    def release_infrared_camera_videostream(self):
        print("Release Infrared Camera Videostream")
        self.model.release_infrared_camera_videostream()

    ############################################################
    # Recording
    ############################################################
    def start_record(self):
        print("Start Record")
        self.model.create_rgb_camera_videostream(camera_index = 2)
        self.model.start_record()

    def stop_record(self):
        print("Stop Record")
        self.model.stop_record()

    ############################################################
    # Close Event
    ############################################################
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
