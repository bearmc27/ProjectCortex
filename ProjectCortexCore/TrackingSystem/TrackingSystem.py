"""
Objective:
- Connect SerialCommunicationController and camera related system together
"""

import SerialCommunicationController.Controller as serial_controller


class TrackingSystem():
    controller_thread = None

    def __init__(self):
        self.controller_thread = serial_controller.Controller()
        self.controller_thread.start()
        pos = input("Next position: ")
        while pos != "exit":
            self.set_controller_thread_message(pos)
            pos = input("Next position: ")
        self.controller_thread.stop()
        print("End of program")

    # TODO: add message checking
    def set_controller_thread_message(self,msg):
        self.controller_thread.set_message(msg)