from PyQt5 import QtGui

from cv2 import cv2


def frame_to_pixmap(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
    pix = QtGui.QPixmap.fromImage(img)

    return pix
