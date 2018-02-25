from threading import Thread

import imutils
import numpy as np
from cv2 import cv2

from CoreMVC.Model.Camera import CameraModel
from CoreMVC.Model.Camera.Camera import Camera
from CoreMVC.Model.Infrared import InfraredModel
from CoreMVC.Model.Serial.SerialConnection import SerialConnection
from CoreMVC.Model.Serial.SerialModel import SerialModel
from CoreMVC.Model.Target.Target import Target
from CoreMVC.Model.Util.Gui import GuiModel


class Model:
    def __init__(self):
        # TODO: move these codes to other place
        # Defines the effective range(boarder), helps avoid tiny noise movement
        self.effective_x = 5
        self.effective_y = 5

        self.serial_connection = None

        self.rgb_camera = None
        self.infrared_camera = None

        self.is_previewing = False
        self.is_tracking = False

    def set_controller(self, controller):
        self.controller = controller

    def main_gui_closeEvent(self):
        self.stop_record()
        self.stop_tracking()
        self.stop_video_preview()
        # TODO: check if the thread is stopped, then Cameras=None
        if self.rgb_camera is not None:
            self.rgb_camera.release_camera()
        self.rgb_camera = None

        if self.infrared_camera is not None:
            self.infrared_camera.release_camera()
        self.infrared_camera = None

        if self.serial_connection is not None:
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
        if self.rgb_camera is None:
            print("RGB Camera Not Yet Setup, Cannot Get Frame")
            return False, None
        else:
            return self.rgb_camera.get_frame()

    def rgb_camera_set_resolution(self, width, height):
        if self.rgb_camera is None:
            print("RGB Camera Not Yet Setup, Cannot Set Resolution")
        else:
            self.rgb_camera.set_videostream_resolution(width = width, height = height)

    ############################################################
    # Infrared Camera
    ############################################################
    def infrared_camera_get_frame(self):
        if self.infrared_camera is None:
            print("Infrared Camera Not Yet Setup, Cannot Get Frame")
            return False, None
        else:
            return self.infrared_camera.get_frame()

    def infrared_camera_set_resolution(self, width, height):
        if self.infrared_camera is None:
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
            if self.rgb_camera is None:
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
        while self.is_previewing and self.rgb_camera is not None:
            ret, frame = self.rgb_camera_get_frame()
            if ret:
                pix = GuiModel.frame_to_pixmap(frame)

                self.controller.main_gui_set_label_videostream_frame(pixmap = pix)

            else:
                print("Preview Ended With ret=False")
                self.is_previewing = False
                self.rgb_camera = None

        self.is_previewing = False
        print("Preview Ended")
        self.controller.main_gui_clear_label_videostream_frame()

    ############################################################
    # Tracking
    ############################################################
    def start_tracking(self):
        if self.is_tracking:
            print("Already Tracking")
        else:
            if self.infrared_camera is None:
                print("Infrared Camera Not Yet Setup")
            else:
                if self.serial_connection is None:
                    print("Serial Communication Have Not Setup")
                else:
                    self.is_tracking = True
                    Thread(target = self.tracking_loop, args = ()).start()

    def stop_tracking(self):
        if self.is_tracking:
            self.is_tracking = False
        else:
            print("Program Was Not Tracking")

    def tracking_loop(self):
        # TODO: Remove these code later

        cv2.namedWindow("Test", cv2.WINDOW_NORMAL)
        blue_image = np.zeros((400, 400, 3), np.uint8)
        red_image = np.zeros((400, 400, 3), np.uint8)
        blue_image[:, 0:400] = (255, 0, 0)
        red_image[:, 0:400] = (0, 0, 255)

        i = 0

        while self.is_tracking and self.infrared_camera is not None:
            # Get a frame from camera
            ret, frame = self.infrared_camera_get_frame()

            if ret:
                # Resize(downsize) the frame for better processing performance
                # Current natively using 320x240 frame, no downsizing it needed
                frame = imutils.resize(frame, width = 320)

                # Process the frame
                ir_result = InfraredModel.find_candidate_targets(frame = frame)
                result = ir_result["result"]
                pro_processing_frame = ir_result["pro_processing_frame"]

                if result:
                    targets = ir_result["targets"]

                    if len(targets) == 1:
                        x, y = targets[0].x, targets[0].y

                    else:
                        targets.sort(key = Target.get_radius, reverse = True)
                        x, y = Target.find_2_targets_middle(target0 = targets[0], target1 = targets[1])

                    # TODO: Remove these code later
                    cv2.imshow("Result", blue_image)
                    cv2.waitKey(1)
                    cv2.circle(pro_processing_frame, (x, y), 2, (0, 255, 0), -1)
                    cv2.imshow("Test", pro_processing_frame)
                    cv2.waitKey(1)

                    # Calculate the distance from center to target, in X-axis and Y-axis
                    dx = x - 160
                    dy = y - 160

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
                        if dx < 0:
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
                        message = "0" + str(direction_x) + str(abs(dx)).zfill(3) + str(direction_y) + str(abs(dy)).zfill(3) + ";"
                        # print("Sent Message: " + message)

                        # Send message
                        self.send_serial_message(message = message)
                        # print(message)

                else:
                    # TODO: Remove these code later
                    cv2.imshow("Result", red_image)
                    cv2.waitKey(1)

            else:
                print("Tracking Ended With ret=False")
                self.is_tracking = False
                self.infrared_camera = None

        cv2.destroyAllWindows()
        print("Tracking Ended")
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
        if self.rgb_camera is not None:
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
        self.clear_infrared_camera()
        self.infrared_camera = Camera(camera_index = index)

    def setup_rgb_camera(self, index):
        self.clear_rgb_camera()
        self.rgb_camera = Camera(camera_index = index)

    def clear_infrared_camera(self):
        self.infrared_camera = None

    def clear_rgb_camera(self):
        self.rgb_camera = None

    def get_available_camera_index_list(self):
        return CameraModel.get_available_camera_index_list()

    ############################################################
    # Infrared Boundary
    ############################################################
    def set_infrared_upper_boundary_hue(self, hue):
        InfraredModel.set_infrared_upper_boundary_hue(hue = hue)

    def set_infrared_upper_boundary_saturation(self, saturation):
        InfraredModel.set_infrared_upper_boundary_saturation(saturation = saturation)

    def set_infrared_upper_boundary_value(self, value):
        InfraredModel.set_infrared_upper_boundary_value(value = value)

    def set_infrared_lower_boundary_hue(self, hue):
        InfraredModel.set_infrared_lower_boundary_hue(hue = hue)

    def set_infrared_lower_boundary_saturation(self, saturation):
        InfraredModel.set_infrared_lower_boundary_saturation(saturation = saturation)

    def set_infrared_lower_boundary_value(self, value):
        InfraredModel.set_infrared_lower_boundary_value(value = value)

    ############################################################
    # Morphological Transformation
    ############################################################
    def set_blur_kernalsize(self, blur_kernalsize):
        InfraredModel.set_blur_kernalsize(blur_kernalsize = blur_kernalsize)

    def set_erode_iteration(self, erode_iterations):
        InfraredModel.set_erode_iterations(erode_iterations = erode_iterations)

    def set_dilate_iteration(self, dilate_iterations):
        InfraredModel.set_dilate_iterations(dilate_iterations = dilate_iterations)
