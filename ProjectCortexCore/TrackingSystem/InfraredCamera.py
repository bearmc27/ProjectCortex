"""
Objective:
- Object class of infrared camera
- Includes infrared processing functions
"""
import cv2
import imutils
import numpy as np


class InfraredCamera():
    camera = None

    def __init__(self, camera_index):
        self.camera = cv2.VideoCapture(camera_index)


    def get_frame(self):
        if self.camera.isOpened():
            (grabbed, frame) = self.camera.read()
            frame = imutils.resize(frame, width = 400)
            return self.process(frame)

            # ir_result = self.process(frame)
            #
            # # If InfraredTracker find a target led
            # if (ir_result != None):
            #
            #     # Circling the target
            #     if (True):
            #         # only proceed if the radius meets a minimum size
            #         if ir_result['radius'] > 5:
            #             # draw the circle and centroid on the frame, then update the list of tracked points
            #             cv2.circle(frame, (int(ir_result['x']), int(ir_result['y'])), int(ir_result['radius']),
            #                        (0, 255, 255), 2)
            #             cv2.circle(frame, ir_result['moment_center'], 5, (0, 0, 255), -1)
            #             # draw line from center of frame to circle
            #             cv2.line(frame, (200, 150), (int(ir_result['x']), int(ir_result['y'])), (255, 0, 0), 2)
            #             print("dx:" + str(int(ir_result['x']) - 200) + "\tdy:" + str(int(ir_result['y']) - 150))

    def process(self,frame):
        # Convert frame from RGB color space to HSV color base
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the boundary of target color in HSV color space
        # Infrared light appear white-ish in frame
        lower_boundary = np.array([0, 0, 220])
        upper_boundary = np.array([100, 60, 255])
        mask = cv2.inRange(frame_hsv, lower_boundary, upper_boundary)

        # Dilate the frame
        mask = cv2.dilate(mask, None, iterations = 3)

        # Find contours in the mask
        # contours: 輪廓
        # cv2.RETR_EXTERNAL: only check the contours
        # cv2.CHAIN_APPROX_SIMPLE: only keep the coordinate value (x, y), ignore directional data
        contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        # If there exists contour
        if len(contours) > 0:
            # Find the largest contour among all contours
            largest_contour = max(contours, key = cv2.contourArea)

            # Form the minimum circle contain the above largest contour
            # Get x, y, and radius of largest contour
            ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

            # Only proceed if the radius meets the minimum size
            if radius > 5:
                # Calculate the moment value of largest contour and find its center
                M = cv2.moments(largest_contour)
                moment_center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                return {'x': x, 'y': y, 'radius': radius, 'moment_center': moment_center}

        return None
