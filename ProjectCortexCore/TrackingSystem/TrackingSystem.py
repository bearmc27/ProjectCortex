"""
Objective:
- Connect SerialCommunicationController and camera related system together
"""

from SerialCommunicationController import Controller as serial_controller
from TrackingSystem import InfraredCamera as infrared_camera


class TrackingSystem():
    controller_thread = None
    ir_camera_thread = None

    def __init__(self):
        # Start serial communication controller thread
        self.controller_thread = serial_controller.Controller()
        self.controller_thread.start()

        # Start infrared camera thread
        self.ir_camera_thread = infrared_camera.InfraredCamera(1)
        while (True):
            ir_result = self.ir_camera_thread.get_frame()
            if (ir_result != None):
                self.set_controller_thread_message("9999")

        print("End of program")

    # TODO: add message checking
    def set_controller_thread_message(self, msg):
        self.controller_thread.set_message(msg)
