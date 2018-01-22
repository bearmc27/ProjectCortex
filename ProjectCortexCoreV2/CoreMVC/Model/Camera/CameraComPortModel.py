import numpy as np
from cv2 import cv2


############################################################
# Camera Com Port
############################################################
def get_camera_com_port_list(range_min = 0, range_max = 2):
    com_port_list = np.full(range_max - range_min + 1, True, dtype = bool)
    for index in range(range_min, range_max):
        com_port_list[index] = check_com_port_with_cv2_VideoCapture(index = index)
    return com_port_list


def check_com_port_with_cv2_VideoCapture(index):
    camera_opened = False
    videostream = cv2.VideoCapture(index)
    if videostream.isOpened():
        camera_opened = True
    videostream.release()

    return camera_opened
