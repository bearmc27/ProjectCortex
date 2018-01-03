import math
import time
from threading import Thread

import imutils
from PyQt5 import QtGui
from cv2 import cv2

from CoreMVC.Model.Camera.InfraredCamera.InfraredCamera import InfraredCamera
from CoreMVC.Model.Camera.RgbCamera.RgbCamera import RgbCamera
from CoreMVC.Model.Serial.SerialModel import SerialModel


class Model():
    def __init__(self):
        # TODO: move these codes to other place
        # Defines the effective range(boarder), helps avoid tiny noise movement
        self.effective_x = 5
        self.effective_y = 5

        self.ratio_x = 1.0
        self.ratio_y = 1.0

        self.record_fps = 1 / 30

        self.serial_model = None
        self.rgb_camera = RgbCamera(camera_index = 2)
        self.infrared_camera = InfraredCamera(camera_index = 1)

        self.rgb_camera.set_videostream_resolution(width = 1280, height = 720)
        self.rgb_camera.set_videostream_resolution(width = 640, height = 360)

    def set_controller(self, controller):
        self.controller = controller

    def set_view(self, view):
        self.view = view

    ############################################################
    # Serial
    ############################################################
    def create_serial_model(self, baudrate, port):
        self.serial_model = SerialModel(baudrate = baudrate, port = port)
        return True

    def send_serial_message(self, message):
        self.serial_model.send_serial_message(message = message)

    ############################################################
    # RGB Camera
    ############################################################
    def rgb_camera_get_frame(self):
        return self.rgb_camera.get_frame()

    ############################################################
    # Infrared Camera
    ############################################################
    def infrared_camera_get_frame(self):
        return self.infrared_camera.get_frame()

    ############################################################
    # Video Preview
    ############################################################
    def start_video_preview(self):
        self.is_previewing = True
        Thread(target = self.view_preview_loop, args = ()).start()

    def stop_video_preview(self):
        self.is_previewing = False

    def view_preview_loop(self):
        while self.is_previewing:
            ret, frame = self.rgb_camera_get_frame()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(img)

                self.view.main_gui_set_label_videostream_frame(pixmap = pix)

                time.sleep(0.05)
            else:
                print("Preview ended with ret=False")
                self.is_previewing = False

    ############################################################
    # Tracking
    ############################################################
    def start_tracking(self):
        self.is_tracking = True
        Thread(target = self.tracking_loop, args = ()).start()

    def stop_tracking(self):
        self.is_tracking = False

    def tracking_loop(self):
        while self.is_tracking:
            # Get a frame from camera
            ret, frame = self.infrared_camera_get_frame()
            if ret:

                # Resize(downsize) the frame for better processing performance
                frame = imutils.resize(frame, width = 320)

                # Process the frame
                ir_result = self.infrared_camera.process(frame = frame)

                # If InfraredTracker find a target led
                if ir_result != None:

                    # only proceed if the radius meets a minimum size
                    if ir_result['radius'] > 5:

                        # Calculate the distance from center to target, in X-axis and Y-axis
                        # dx = math.floor((int(ir_result['x']) - 200) * self.ratio)
                        # dy = math.floor((int(ir_result['y']) - 150) * self.ratio)
                        dx = int(ir_result['x']) - 160
                        dy = int(ir_result['y']) - 160

                        # print("Before: dx: " + str(dx) + "\tdy: " + str(dy))

                        abs_dx = abs(dx)
                        abs_dy = abs(dy)
                        if abs_dx < self.effective_x:
                            dx = 0
                        if abs_dy < self.effective_y:
                            dy = 0

                        # print("After : dx: " + str(dx) + "\tdy: " + str(dy))

                        if not (dx == 0 and dy == 0):

                            # 0 = Negative, 2 = Positive, this value will be minus 1 in Arduino board, 0-> -1; 2-> 1
                            # target on left to center
                            if (dx < 0):
                                direction_x = 0
                            # target on right to center
                            else:
                                direction_x = 2
                            # target above center
                            if dy < 0:
                                direction_y = 0
                            # target below center
                            else:
                                direction_y = 2

                            # TODO: Set package type
                            # Build the message string
                            # First integer is package type
                            message = "0" + str(direction_x) + str(math.floor(abs(dx) * self.ratio_x)).zfill(3) + str(direction_y) + str(math.floor(abs(dy) * self.ratio_y)).zfill(3) + ";"
                            # print("Sent Message: " + message)

                            # Send message
                            # self.send_serial_message(message = message)
                            print(message)
            else:
                print("Tracking ended with ret=False")
                self.is_tracking = False

    ############################################################
    # Recording
    ############################################################
    def start_record(self):
        # TODO: Relocate these code
        fourcc_codex = cv2.VideoWriter_fourcc(*"FFV1")
        self.rgb_camera.create_record_videowriter(codex = fourcc_codex, video_path = "output.avi", fps = 30.0)
        self.rgb_camera.start_record()

    def stop_record(self):
        self.rgb_camera.stop_record()
