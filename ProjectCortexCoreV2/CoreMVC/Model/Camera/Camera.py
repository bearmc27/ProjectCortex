from threading import Thread

from cv2 import cv2


class Camera():
    def __init__(self, camera_index):
        self.camera_index = camera_index
        self.videostream = cv2.VideoCapture(camera_index)
        self.is_recording = False
        self.video_out = None

        self.is_recording = False

        # Do a test frame reading
        ret, frame = self.videostream.read()
        print(ret)


        # TODO: check self.grabbed to see videostream setup correctly

    ############################################################
    # Video Stream
    ############################################################
    def get_frame(self):
        if self.videostream.isOpened():
            # ret, frame
            return self.videostream.read()

    def get_videostream_resolution(self):
        width = self.videostream.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.videostream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return width, height

    def set_videostream_resolution(self, width, height):
        self.videostream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.videostream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def create_record_videowriter(self, codex, video_path, fps):
        width, height = self.get_videostream_resolution()
        self.video_out = cv2.VideoWriter(video_path, codex, fps, (int(width), int(height)))

    ############################################################
    # Recording
    ############################################################
    def start_record(self):
        if self.is_recording:
            print("Already Recording")
        else:
            self.is_recording = True
            Thread(target = self.record_loop, args = ()).start()

    def stop_record(self):
        self.is_recording = False

    def record_loop(self):
        while self.is_recording:
            ret, frame = self.get_frame()
            if ret:
                # Write the frame
                self.video_out.write(frame)

            else:
                self.is_recording = False

        self.video_out.release()

        # TODO: pro-recording work here, e.g. file naming...

    ############################################################
    # Other
    ############################################################
    def release_camera(self):
        self.videostream.release()
