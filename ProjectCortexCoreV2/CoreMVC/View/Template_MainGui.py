# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Template_MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainGui(object):
    def setupUi(self, MainGui):
        MainGui.setObjectName("MainGui")
        MainGui.resize(700, 500)
        self.button_start_preview = QtWidgets.QPushButton(MainGui)
        self.button_start_preview.setGeometry(QtCore.QRect(10, 460, 100, 30))
        self.button_start_preview.setObjectName("button_start_preview")
        self.button_stop_preview = QtWidgets.QPushButton(MainGui)
        self.button_stop_preview.setGeometry(QtCore.QRect(120, 460, 100, 30))
        self.button_stop_preview.setObjectName("button_stop_preview")
        self.label_videostream = QtWidgets.QLabel(MainGui)
        self.label_videostream.setGeometry(QtCore.QRect(30, 10, 640, 360))
        self.label_videostream.setText("")
        self.label_videostream.setPixmap(QtGui.QPixmap("../../../../../Users/man_k/Desktop/sample_picture_1080p.jpg"))
        self.label_videostream.setScaledContents(True)
        self.label_videostream.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_videostream.setObjectName("label_videostream")
        self.button_start_tracking = QtWidgets.QPushButton(MainGui)
        self.button_start_tracking.setGeometry(QtCore.QRect(230, 460, 100, 30))
        self.button_start_tracking.setObjectName("button_start_tracking")
        self.button_stop_tracking = QtWidgets.QPushButton(MainGui)
        self.button_stop_tracking.setGeometry(QtCore.QRect(340, 460, 100, 30))
        self.button_stop_tracking.setObjectName("button_stop_tracking")
        self.button_release_rgb_camera_videostream = QtWidgets.QPushButton(MainGui)
        self.button_release_rgb_camera_videostream.setGeometry(QtCore.QRect(10, 420, 211, 30))
        self.button_release_rgb_camera_videostream.setObjectName("button_release_rgb_camera_videostream")
        self.button_release_infrared_camera_videostream = QtWidgets.QPushButton(MainGui)
        self.button_release_infrared_camera_videostream.setGeometry(QtCore.QRect(230, 420, 211, 30))
        self.button_release_infrared_camera_videostream.setObjectName("button_release_infrared_camera_videostream")
        self.button_start_record = QtWidgets.QPushButton(MainGui)
        self.button_start_record.setGeometry(QtCore.QRect(10, 380, 100, 30))
        self.button_start_record.setObjectName("button_start_record")
        self.button_stop_record = QtWidgets.QPushButton(MainGui)
        self.button_stop_record.setGeometry(QtCore.QRect(120, 380, 100, 30))
        self.button_stop_record.setObjectName("button_stop_record")

        self.retranslateUi(MainGui)
        QtCore.QMetaObject.connectSlotsByName(MainGui)

    def retranslateUi(self, MainGui):
        _translate = QtCore.QCoreApplication.translate
        MainGui.setWindowTitle(_translate("MainGui", "Form"))
        self.button_start_preview.setText(_translate("MainGui", "Start Preview"))
        self.button_stop_preview.setText(_translate("MainGui", "Stop Preview"))
        self.button_start_tracking.setText(_translate("MainGui", "Start Tracking"))
        self.button_stop_tracking.setText(_translate("MainGui", "Stop Tracking"))
        self.button_release_rgb_camera_videostream.setText(_translate("MainGui", "Release RGB Camera videostream"))
        self.button_release_infrared_camera_videostream.setText(_translate("MainGui", "Release Infrared Camera videostream"))
        self.button_start_record.setText(_translate("MainGui", "Start Record"))
        self.button_stop_record.setText(_translate("MainGui", "Stop Recording"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainGui = QtWidgets.QWidget()
    ui = Ui_MainGui()
    ui.setupUi(MainGui)
    MainGui.show()
    sys.exit(app.exec_())
