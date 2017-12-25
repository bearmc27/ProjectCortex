"""
Objective:
- Object class of infrared camera
- Includes infrared processing functions
"""
import cv2
import numpy as np

from InfraredCamera.VideoStream import VideoStream


class Camera():
    def __init__(self, camera_index):
        self.video_stream = VideoStream(src = camera_index)
        self.video_stream.start()

    def get_frame(self):
        return self.video_stream.get_frame()

    def process(self, frame):
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
