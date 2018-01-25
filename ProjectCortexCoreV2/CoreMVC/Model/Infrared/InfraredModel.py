import numpy as np
from cv2 import cv2

lower_boundary = np.array([0, 0, 200])
upper_boundary = np.array([100, 60, 255])


def set_lower_boundary(boundary):
    """
    boundary should be numpy array with 3 fields [Hue, Saturation, Value]

    Hue: 0-179

    Saturation: 0-255

    Value: 0-255
    """
    global lower_boundary
    lower_boundary = boundary


def set_upper_boundary(boundary):
    """
    boundary should be numpy array with 3 fields [Hue, Saturation, Value]

    Hue: 0-179

    Saturation: 0-255

    Value: 0-255
    """
    global upper_boundary
    upper_boundary = boundary


def find_largest_contour(frame):
    # Blur the frame to remove noise
    frame_pre_blur = cv2.medianBlur(frame, 5)

    # Convert frame from RGB color space to HSV color base
    frame_hsv = cv2.cvtColor(frame_pre_blur, cv2.COLOR_BGR2HSV)

    # Define the boundary of target color in HSV color space
    # Infrared light appear white-ish in frame
    mask = cv2.inRange(frame_hsv, lower_boundary, upper_boundary)

    # Eroded the frmae
    # mask_eroded = cv2.erode(mask, None, iterations=1)

    # Dilate the frame
    mask_dilated = cv2.dilate(mask, None, iterations = 10)

    # Find contours in the mask
    # contours: 輪廓
    # cv2.RETR_EXTERNAL: only check the contours
    # cv2.CHAIN_APPROX_SIMPLE: only keep the coordinate value (x, y), ignore directional data
    contours = cv2.findContours(mask_dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # If there exists contour
    if len(contours) > 0:

        # Find the largest contour among all contours
        largest_contour = max(contours, key = cv2.contourArea)

        # Form the minimum circle contain the above largest contour
        # Get x, y, and radius of largest contour
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

        # Only proceed if the radius meets the minimum size
        if radius > 5:
            # Calculate the centroid of largest contour and find its center
            M = cv2.moments(largest_contour)
            centroid_x = int(M["m10"] / M["m00"])
            centroid_y = int(M["m01"] / M["m00"])

            return {"result": True, 'x': x, 'y': y, 'radius': radius, 'centroid_x': centroid_x, "centroid_y": centroid_y, "pro_processing_frame": mask}

    return {"result": False, "pro_processing_frame": mask_dilated}
