from threading import Thread

from cv2 import cv2


class Camera():
    def __init__(self):
        pass

    ############################################################
    # Video Stream
    ############################################################
    def create_videostream(self, camera_index):
        self.videostream = Videostream(camera_index = camera_index)

    def start_stream(self):
        self.videostream.start_stream()

    def stop_stream(self):
        self.videostream.stop_stream()

    def get_frame(self):
        return self.videostream.get_frame()


class Videostream():
    def __init__(self, camera_index):
        self.camera_index = camera_index
        self.videostream = cv2.VideoCapture(self.camera_index)

        # Do a test frame reading
        (self.grabbed, self.frame) = self.videostream.read()

        # Default flag set to False (Thread running)
        self.is_videostreaming = True

    def start_stream(self):
        # Start the thread to read frames from web cam video stream
        Thread(target = self.run, args = ()).start()

    def stop_stream(self):
        # Indicate the thread to be stopped
        self.is_videostreaming = False

    def run(self):
        # If thread is not stopped, get a new frame from web cam video stream
        while self.is_videostreaming:
            if self.videostream.isOpened():
                (self.grabbed, self.frame) = self.videostream.read()

    def get_frame(self):
        # Return the most recent frame
        return self.frame
