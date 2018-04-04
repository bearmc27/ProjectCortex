from threading import Thread

import imutils
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

        self.rgb_camera_index = None
        self.infrared_camera_index = None

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
        self.clear_rgb_camera()

        if self.infrared_camera is not None:
            self.infrared_camera.release_camera()
        self.clear_infrared_camera()

        if self.serial_connection is not None:
            self.serial_connection.close_serial()
            self.serial_connection = None

    ############################################################
    # Serial
    ############################################################
    def create_serial_connection(self, baudrate, port):
        if self.serial_connection is None:
            self.serial_connection = SerialConnection(baudrate = baudrate, port = port)
            self.controller.view.set_label_status_serial_connection_text("online")

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
                self.controller.view.disable_button_start_preview()
                self.controller.view.enable_button_stop_preview()

    def stop_video_preview(self):
        if self.is_previewing:
            self.is_previewing = False
            self.controller.view.disable_button_stop_preview()
            self.controller.view.enable_button_start_preview()
        else:
            print("Program Was Not Previewing")

    def view_preview_loop(self):
        while self.is_previewing:
            if self.rgb_camera is not None:
                ret, frame = self.rgb_camera_get_frame()
                if ret:
                    pix = GuiModel.frame_to_pixmap(frame)

                    self.controller.main_gui_set_label_rgb_camera_preview_frame(pixmap = pix)

                else:
                    print("Preview Ended With ret=False")
                    self.stop_video_preview()
            else:
                print("Preview Ended With rgb_camera is None")
                self.stop_video_preview()

        print("Preview Ended")
        self.controller.main_gui_clear_label_rgb_camera_preview_frame()

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
                # TODO: remove "and False" when using actual serial connection.
                if self.serial_connection is None:
                    print("Serial Communication Have Not Setup")
                else:
                    self.is_tracking = True
                    Thread(target = self.tracking_loop, args = ()).start()
                    self.controller.view.disable_button_start_tracking()
                    self.controller.view.enable_button_stop_tracking()

    def stop_tracking(self):
        if self.is_tracking:
            self.is_tracking = False
            self.controller.view.disable_button_stop_tracking()
            self.controller.view.enable_button_start_tracking()
        else:
            print("Program Was Not Tracking")

    def tracking_loop(self):

        while self.is_tracking:
            if self.infrared_camera is not None:
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
                            cv2.circle(pro_processing_frame, (x, y), 6, (0, 0, 255), -1)

                        else:
                            # sort the candidates by radius
                            targets.sort(key = Target.get_radius, reverse = True)

                            # if the largest candidates is larger than the second largest candidates by a lot (* 0.??, hence ??% )
                            # We can assume that the anything other than the largest candidates should be considered.
                            if targets[1].radius < (targets[0].radius * 0.15):
                                x, y = targets[0].x, targets[0].y
                                cv2.circle(pro_processing_frame, (x, y), 6, (0, 0, 255), -1)
                            else:
                                # Both first and second largest candidates are large enough, compare to each other, hence consider both.
                                x, y = Target.find_2_targets_middle(target0 = targets[0], target1 = targets[1])
                                cv2.circle(pro_processing_frame, (targets[0].x, targets[0].y), 6, (0, 0, 255), -1)
                                cv2.circle(pro_processing_frame, (targets[1].x, targets[1].y), 6, (0, 0, 255), -1)

                        cv2.circle(pro_processing_frame, (x, y), 4, (0, 255, 0), -1)
                        pix = GuiModel.frame_to_pixmap(pro_processing_frame)
                        self.controller.main_gui_set_label_infrared_camera_preview_frame(pixmap = pix)

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
                            message = "0" + str(direction_x) + str(abs(dx)).zfill(3) + str(direction_y) + str(abs(dy)).zfill(3) + ";"  # print("Sent Message: " + message)

                            # Send message
                            self.send_serial_message(message = message)
                            print(message)

                    else:
                        pix = GuiModel.frame_to_pixmap(pro_processing_frame)
                        self.controller.main_gui_set_label_infrared_camera_preview_frame(pixmap = pix)

                else:
                    print("Tracking Ended With ret=False")
                    self.stop_tracking()  # self.infrared_camera = None
            else:
                print("Tracking Ended With infrared_camera is None")
                self.stop_tracking()

        print("Tracking Ended")
        self.controller.main_gui_clear_label_infrared_camera_preview_frame()

    ############################################################
    # Recording
    ############################################################
    def start_record(self):
        # TODO: Relocate these code
        if self.rgb_camera is None:
            print("RGB Camera Not Yet Setup")
        else:
            if self.rgb_camera.start_record(model = self):
                self.controller.view.disable_button_start_record()
                self.controller.view.enable_button_stop_record()

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
        if self.serial_connection is not None:
            self.send_serial_message(message = "000000010;")

    def manual_gimbal_down(self):
        if self.serial_connection is not None:
            self.send_serial_message(message = "000002010;")

    def manual_gimbal_left(self):
        if self.serial_connection is not None:
            self.send_serial_message(message = "000100000;")

    def manual_gimbal_right(self):
        if self.serial_connection is not None:
            self.send_serial_message(message = "020100000;")

    ############################################################
    # Camera Setup
    ############################################################
    def setup_infrared_camera(self, index):
        if self.is_tracking:
            self.stop_tracking()

        self.clear_infrared_camera()
        self.infrared_camera_index = index
        if self.rgb_camera is not None:
            if self.rgb_camera.camera_index == index:
                self.infrared_camera = self.rgb_camera
                self.controller.view.set_label_status_infrared_camera_text("online")

                self.controller.view.enable_button_start_tracking()
                return
        self.infrared_camera = Camera(camera_index = index)
        self.controller.view.set_label_status_infrared_camera_text("online")

        self.controller.view.enable_button_start_tracking()

    def setup_rgb_camera(self, index):
        if self.is_previewing:
            self.stop_video_preview()

        if self.rgb_camera is not None:
            if self.rgb_camera.is_recording:
                self.rgb_camera.stop_record()

        self.clear_rgb_camera()
        self.rgb_camera_index = index
        if self.infrared_camera is not None:
            if self.infrared_camera.camera_index == index:
                self.rgb_camera = self.infrared_camera
                self.controller.view.set_label_status_rgb_camera_text("online")

                self.controller.view.enable_button_start_preview()
                self.controller.view.enable_button_start_record()
                return
        self.rgb_camera = Camera(camera_index = index)
        self.controller.view.set_label_status_rgb_camera_text("online")

        self.controller.view.enable_button_start_preview()
        self.controller.view.enable_button_start_record()

    def clear_infrared_camera(self):
        self.infrared_camera = None
        self.controller.view.set_label_status_infrared_camera_text("offline")

    def clear_rgb_camera(self):
        self.rgb_camera = None
        self.controller.view.set_label_status_rgb_camera_text("offline")

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
