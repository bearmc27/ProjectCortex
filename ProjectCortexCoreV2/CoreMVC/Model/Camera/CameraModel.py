from cv2 import cv2


############################################################
# Camera Com Port
############################################################
def get_available_camera_index_list():
    index = 0
    list = []
    while True:
        if check_index_with_cv2_VideoCapture(index):
            list.append(str(index))
            index = index + 1
        else:
            break
    return list


def check_index_with_cv2_VideoCapture(index):
    camera_opened = False
    videostream = cv2.VideoCapture(index)
    if videostream.isOpened():
        camera_opened = True
    videostream.release()

    return camera_opened
