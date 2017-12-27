from threading import Thread

import cv2
import time

class VideoStream:
    def __init__(self, src = 0):
        self.stream = cv2.VideoCapture(src)

        # Do a test frame reading
        (self.grabbed, self.frame) = self.stream.read()

        # Default flag set to False (Thread running)
        self.stopped = False

    def start(self):
        # Start the thread to read frames from web cam video stream
        Thread(target = self.run, args = ()).start()

    def run(self):
        # If thread is not stopped, get a new frame from web cam video stream
        while not self.stopped:
            if self.stream.isOpened():
                (self.grabbed, self.frame) = self.stream.read()


    def get_frame(self):
        # Return the most recent frame
        return self.frame

    def stop(self):
        # Indicate the thread to be stopped
        self.stopped = True
