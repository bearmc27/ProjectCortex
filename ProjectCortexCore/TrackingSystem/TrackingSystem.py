"""
Objective:
- Connect SerialCommunicationController and camera related system together
"""

import imutils

from InfraredCamera import Camera as infrared_camera
from SerialCommunicationController import Controller as serial_controller


class TrackingSystem:
    def __init__(self):
        # Start serial communication controller thread
        self.controller = serial_controller.Controller()
        # self.controller_thread.start()

        # Start infrared camera thread
        self.ir_camera = infrared_camera.Camera(camera_index = 0)
        while True:
            # Get a frame from camera
            frame = imutils.resize(self.ir_camera.get_frame(), width = 400)

            # Process the frame
            ir_result = self.ir_camera.process(frame)

            # If InfraredTracker find a target led
            if ir_result != None:

                # only proceed if the radius meets a minimum size
                if ir_result['radius'] > 5:

                    # Calculate the distance from center to target, in X-axis and Y-axis
                    dx = int(ir_result['x']) - 200
                    dy = int(ir_result['y']) - 150
                    # Print the value of DX and DY
                    print("dx:" + str(dx) + "\tdy:" + str(dy))

                    # 0 = Negative, 2 = Positive, this value will be minus 1 in Arduino board, 0-> -1, 2-> 1
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
                    message = "0" + str(direction_x) + str(abs(dx)).zfill(3) + str(direction_y) + str(abs(dy)).zfill(3) + ";"
                    print("Message is now: " + message)

                    # Send message
                    self.send_serial_message(message = message)

    # Pass the message to SerialCommunicationController
    def send_serial_message(self, message):
        self.controller.send_serial_message(message = message)
