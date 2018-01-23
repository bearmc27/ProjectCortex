import math
from threading import Thread

from PyQt5 import QtGui
from cv2 import cv2

from CoreMVC.Model.Camera import CameraModel
from CoreMVC.Model.Camera.Camera import Camera
from CoreMVC.Model.InfraredModel import InfraredModel
from CoreMVC.Model.Serial.SerialConnection import SerialConnection
from CoreMVC.Model.Serial.SerialModel import SerialModel


class Model():
    def __init__(self):
        # TODO: move these codes to other place
        # Defines the effective range(boarder), helps avoid tiny noise movement
        self.effective_x = 5
        self.effective_y = 5

        self.ratio_x = 1.0
        self.ratio_y = 1.0

        self.serial_connection = None

        print(CameraModel.get_available_camera_index_list())

        # self.rgb_camera = Camera(camera_index = 1)
        # self.infrared_camera = Camera(camera_index = 1)
        self.rgb_camera = None
        self.infrared_camera = None
        # self.rgb_camera.set_videostream_resolution(width = 1920, height = 1080)
        # self.infrared_camera.set_videostream_resolution(width = 320, height = 240)


        self.is_previewing = False
        self.is_tracking = False

    def set_controller(self, controller):
        self.controller = controller

    def main_gui_closeEvent(self):
        self.stop_record()
        self.stop_tracking()
        self.stop_video_preview()
        # TODO: check if the thread is stopped, then Cameras=None
        if self.rgb_camera != None:
            self.rgb_camera.release_camera()
        self.rgb_camera = None

        if self.infrared_camera != None:
            self.infrared_camera.release_camera()
        self.infrared_camera = None

        if self.serial_connection != None:
            self.serial_connection.close_serial()
            self.serial_connection = None

    ############################################################
    # Serial
    ############################################################
    def create_serial_connection(self, baudrate, port):
        if self.serial_connection is None:
            self.serial_connection = SerialConnection(baudrate = baudrate, port = port)

        else:
            print("Serial Model Already Created @" + str(self.serial_connection.get_port()) + " " + str(self.serial_connection.get_baudrate()) + " baud")

    def send_serial_message(self, message):
        self.serial_connection.send_serial_message(message = message)

    def get_available_serial_ports_list(self):
        return SerialModel.get_available_serial_ports_list()

    ############################################################
    # RGB Camera
    ############################################################
    def rgb_camera_get_frame(self):
        if self.rgb_camera == None:
            print("RGB Camera Not Yet Setup, Cannot Get Frame")
            return False, None
        else:
            return self.rgb_camera.get_frame()

    def rgb_camera_set_resolution(self, width, height):
        if self.rgb_camera == None:
            print("RGB Camera Not Yet Setup, Cannot Set Resolution")
        else:
            self.rgb_camera.set_videostream_resolution(width = width, height = height)

    ############################################################
    # Infrared Camera
    ############################################################
    def infrared_camera_get_frame(self):
        if self.infrared_camera == None:
            print("Infrared Camera Not Yet Setup, Cannot Get Frame")
            return False, None
        else:
            return self.infrared_camera.get_frame()

    def infrared_camera_set_resolution(self, width, height):
        if self.infrared_camera == None:
            print("Infrared Camera Not Yet Setup, Cannot Set Resolution")
        else:
            self.infrared_camera.set_videostream_resolution(width = width, height = height)

    ############################################################
    # Video Preview
    ############################################################
    def start_video_preview(self):
        if self.is_previewing:
            print("Already Previewing")
        else:
            if self.rgb_camera == None:
                print("RGB Camera Not Yet Setup")
            else:
                self.is_previewing = True
                Thread(target = self.view_preview_loop, args = ()).start()

    def stop_video_preview(self):
        if self.is_previewing:
            self.is_previewing = False
        else:
            print("Program Was Not Previewing")

    def view_preview_loop(self):
        while self.is_previewing:
            ret, frame = self.rgb_camera_get_frame()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
                pix = QtGui.QPixmap.fromImage(img)

                self.controller.main_gui_set_label_videostream_frame(pixmap = pix)

            else:
                print("Preview ended with ret=False")
                self.is_previewing = False
                self.rgb_camera = None

        self.controller.main_gui_clear_label_videostream_frame()

    ############################################################
    # Tracking
    ############################################################
    def start_tracking(self):
        if self.is_tracking:
            print("Already Tracking")
        else:
            if self.infrared_camera == None:
                print("Infrared Camera Not Yet Setup")
            else:
                if self.serial_connection == None:
                    print("Serial Communication have not setup")
                else:
                    self.is_tracking = True
                    Thread(target = self.tracking_loop, args = ()).start()

    def stop_tracking(self):
        if self.is_tracking:
            self.is_tracking = False
        else:
            print("Program Was Not Tracking")

    def tracking_loop(self):
        while self.is_tracking:
            # Get a frame from camera
            ret, frame = self.infrared_camera_get_frame()

            if ret:
                # Resize(downsize) the frame for better processing performance
                # Current natively using 320x240 frame, no downsizing it needed
                # frame = imutils.resize(frame, width = 320)

                # Process the frame
                ir_result = InfraredModel.process(frame = frame)

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
        fourcc_codex = cv2.VideoWriter_fourcc(*"DIVX")
        self.rgb_camera.create_record_videowriter(codex = fourcc_codex, video_path = "C:/ProjectCortexVideoOutput/output.avi", fps = 30)
        self.rgb_camera.start_record()

    def stop_record(self):
        if self.rgb_camera != None:
            self.rgb_camera.stop_record()

    ############################################################
    # Manual Control
    ############################################################

    ############################################################
    # Manual Control - Gimbal Control
    ############################################################

    def manual_gimbal_up(self):
        self.send_serial_message(message = "000000010;")

    def manual_gimbal_down(self):
        self.send_serial_message(message = "000002010;")

    def manual_gimbal_left(self):
        self.send_serial_message(message = "000100000;")

    def manual_gimbal_right(self):
        self.send_serial_message(message = "020100000;")

    ############################################################
    # Camera Setup
    ############################################################
    def setup_infrared_camera(self, index):
        # self.
        self.infrared_camera = Camera(camera_index = index)

    def setup_rgb_camera(self, index):
        self.rgb_camera = Camera(camera_index = index)

    def get_available_camera_index_list(self):
        return CameraModel.get_available_camera_index_list()
