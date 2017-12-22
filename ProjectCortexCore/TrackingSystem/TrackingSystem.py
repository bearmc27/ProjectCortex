"""
Objective:
- Connect SerialCommunicationController and camera related system together
"""

# from SerialCommunicationController import Controller as serial_controller
from TrackingSystem import InfraredCamera as infrared_camera
import cv2
import imutils
import math


class TrackingSystem():
    controller_thread = None
    ir_camera = None

    def __init__(self):
        # # Start serial communication controller thread
        # self.controller_thread = serial_controller.Controller()
        # self.controller_thread.start()

        # Start infrared camera thread
        self.ir_camera = infrared_camera.InfraredCamera(1)
        while (True):
            # Get a frame from camera
            frame = imutils.resize(self.ir_camera.get_frame(), width = 400)

            # Process the frame
            ir_result = self.ir_camera.process(frame)

            # If InfraredTracker find a target led
            if (ir_result != None):

                # Circling the target
                if (True):
                    # only proceed if the radius meets a minimum size
                    if ir_result['radius'] > 5:

                        # Print the value of DX and DY
                        print("dx:" + str(int(ir_result['x']) - 200) + "\tdy:" + str(int(ir_result['y']) - 150))

                        dx = 0
                        dy = 0
                        if (int(ir_result['x']) - 200 > 0):
                            dx = 32
                        else:
                            dx = -32
                        if (int(ir_result['y']) - 150 > 0):
                            dy = 32
                        else:
                            dy = -32
                        # self.set_controller_thread_message(dx, dy)

        print("End of program")

    # TODO: add message checking
    def set_controller_thread_message(self, dx, dy):
        self.controller_thread.set_message(dx = dx, dy = dy)
