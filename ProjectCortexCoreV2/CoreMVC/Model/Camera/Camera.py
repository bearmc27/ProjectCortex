from threading import Thread

from cv2 import cv2


class Camera():
    def __init__(self):
        self.videostream = None
        self.videostream_number_in_use = 0

    ############################################################
    # Video Stream
    ############################################################
    def create_videostream(self, camera_index):
        if self.videostream == None:
            self.videostream = Videostream(camera_index = camera_index)
        else:
            print("Video Stream already exist, cannot create videostream")

    def start_stream(self):
        if self.videostream == None:
            print("Video Stream not yet create, cannot start videostream")
        else:
            self.videostream.start_stream()

    def stop_stream(self):
        if self.videostream == None:
            print("Video Stream not yet create, cannot stop videostream")
        else:
            self.videostream.stop_stream()

    def get_frame(self):
        if self.videostream == None:
            print("Video Stream not yet create, cannot get frame")
            return None
        else:
            return self.videostream.get_frame()

    def release_videostream(self):
        if self.videostream == None:
            print("Video Stream not yet create, cannot release videostream")
        else:
            if self.videostream_number_in_use > 0:
                print(str(self.videostream_number_in_use) + " thread(s) is using this videostream, cannot release videostream")
            else:
                self.videostream = None

    def add_in_use(self):
        self.videostream_number_in_use += 1

    def reduce_in_use(self):
        self.videostream_number_in_use -= 1

    def get_videostream_resolution(self):
        if self.videostream == None:
            print("Video Stream not yet create, cannot get videostream resolution")
        else:
            return self.videostream.get_videostream_resolution()


class Videostream():
    def __init__(self, camera_index):
        self.camera_index = camera_index
        self.videostream = cv2.VideoCapture(self.camera_index)
        self.videostream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.videostream.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

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

    def release_videostream(self):
        self.videostream.release()

    def get_videostream_resolution(self):
        width = self.videostream.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.videostream.get(cv2.CAP_PROP_FRAME_HEIGHT)
        return width, height
