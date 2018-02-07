import numpy as np
from cv2 import cv2

lower_boundary = np.array([0, 0, 0])
upper_boundary = np.array([0, 0, 0])
_is_erode = False
_erode_iterations = 0
_is_dilate = False
_dilate_iterations = 0
_is_blur = False
_blur_kernalsize = 0


############################################################
# Infrared Boundary
############################################################
def set_infrared_upper_boundary_hue(hue):
    upper_boundary[0] = hue


def set_infrared_upper_boundary_saturation(saturation):
    upper_boundary[1] = saturation


def set_infrared_upper_boundary_value(value):
    upper_boundary[2] = value


def set_infrared_lower_boundary_hue(hue):
    lower_boundary[0] = hue


def set_infrared_lower_boundary_saturation(saturation):
    lower_boundary[1] = saturation


def set_infrared_lower_boundary_value(value):
    lower_boundary[2] = value


############################################################
# Morphological Transformation
############################################################
def set_blur_kernalsize(blur_kernalsize):
    global _blur_kernalsize
    global _is_blur
    offset = blur_kernalsize - 1
    if offset < 0:
        offset = 0
    _blur_kernalsize = blur_kernalsize + offset
    if blur_kernalsize == 0:
        _is_blur = False
    else:
        _is_blur = True


def set_erode_iterations(erode_iterations):
    global _erode_iterations
    global _is_erode
    _erode_iterations = erode_iterations
    if erode_iterations == 0:
        _is_erode = False
    else:
        _is_erode = True


def set_dilate_iterations(dilate_iterations):
    global _dilate_iterations
    global _is_dilate
    _dilate_iterations = dilate_iterations
    if dilate_iterations == 0:
        _is_dilate = False
    else:
        _is_dilate = True


############################################################
# Model
############################################################
def find_largest_contour(frame):
    _frame = frame
    # Blur the frame to remove noise
    if _is_blur:
        _frame = cv2.medianBlur(_frame, _blur_kernalsize)

    # Convert frame from RGB color space to HSV color base
    frame_hsv = cv2.cvtColor(_frame, cv2.COLOR_BGR2HSV)

    # Define the boundary of target color in HSV color space
    # Infrared light appear white-ish in frame
    mask = cv2.inRange(frame_hsv, lower_boundary, upper_boundary)

    # Eroded the frmae
    if _is_erode:
        mask = cv2.erode(mask, None, iterations=_erode_iterations)

    # Dilate the frame
    if _is_dilate:
        mask = cv2.dilate(mask, None, iterations=_dilate_iterations)

    # Find contours in the mask
    # contours: 輪廓
    # cv2.RETR_EXTERNAL: only check the contours
    # cv2.CHAIN_APPROX_SIMPLE: only keep the coordinate value (x, y), ignore directional data
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # If there exists contour
    if len(contours) > 0:

        # Find the largest contour among all contours
        largest_contour = max(contours, key=cv2.contourArea)

        # Form the minimum circle contain the above largest contour
        # Get x, y, and radius of largest contour
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

        # Only proceed if the radius meets the minimum size
        if radius > 2:
            # Calculate the centroid of largest contour and find its center
            M = cv2.moments(largest_contour)

            m00 = M["m00"]
            if m00 == 0:
                centroid_x = 0
                centroid_y = 0
            else:
                centroid_x = int(M["m10"] / m00)
                centroid_y = int(M["m01"] / m00)

            return {"result": True, 'x': x, 'y': y, 'radius': radius, 'centroid_x': centroid_x, "centroid_y": centroid_y, "pro_processing_frame": mask}

    return {"result": False, "pro_processing_frame": mask}
