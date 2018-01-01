"""
Objective:
- Connect SerialCommunicationController and camera related system together
"""

import math

import imutils

from InfraredCamera import Camera as infrared_camera
from SerialCommunicationController import Controller as serial_controller


class TrackingSystem:
    def __init__(self):
        # Defines the effective range(boarder), helps avoid tiny noise movement
        self.effective_x = 10
        self.effective_y = 10

        self.ratio_x = 1.0
        self.ratio_y = 1.25

        # Start serial communication controller thread
        self.serial_controller = serial_controller.Controller()
        # self.controller_thread.start()

        # Start infrared camera thread
        self.ir_camera = infrared_camera.Camera(camera_index = 0)
        while True:
            # Get a frame from camera
            frame = imutils.resize(self.ir_camera.get_frame(), width = 360)

            # Process the frame
            ir_result = self.ir_camera.process(frame)

            # If InfraredTracker find a target led
            if ir_result != None:

                # only proceed if the radius meets a minimum size
                if ir_result['radius'] > 5:

                    # Calculate the distance from center to target, in X-axis and Y-axis
                    # dx = math.floor((int(ir_result['x']) - 200) * self.ratio)
                    # dy = math.floor((int(ir_result['y']) - 150) * self.ratio)
                    dx = int(ir_result['x']) - 180
                    dy = int(ir_result['y']) - 180

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
                        self.send_serial_message(message = message)

    # Pass the message to SerialCommunicationController
    def send_serial_message(self, message):
        self.serial_controller.send_serial_message(message = message)
