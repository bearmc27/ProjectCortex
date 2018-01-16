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
        MainGui.resize(660, 550)
        self.button_start_preview = QtWidgets.QPushButton(MainGui)
        self.button_start_preview.setGeometry(QtCore.QRect(10, 420, 100, 30))
        self.button_start_preview.setObjectName("button_start_preview")
        self.button_stop_preview = QtWidgets.QPushButton(MainGui)
        self.button_stop_preview.setGeometry(QtCore.QRect(120, 420, 100, 30))
        self.button_stop_preview.setObjectName("button_stop_preview")
        self.label_videostream = QtWidgets.QLabel(MainGui)
        self.label_videostream.setGeometry(QtCore.QRect(10, 10, 640, 360))
        self.label_videostream.setAutoFillBackground(True)
        self.label_videostream.setText("")
        self.label_videostream.setScaledContents(True)
        self.label_videostream.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_videostream.setObjectName("label_videostream")
        self.button_start_tracking = QtWidgets.QPushButton(MainGui)
        self.button_start_tracking.setGeometry(QtCore.QRect(10, 460, 101, 30))
        self.button_start_tracking.setObjectName("button_start_tracking")
        self.button_stop_tracking = QtWidgets.QPushButton(MainGui)
        self.button_stop_tracking.setGeometry(QtCore.QRect(120, 460, 100, 30))
        self.button_stop_tracking.setObjectName("button_stop_tracking")
        self.button_start_record = QtWidgets.QPushButton(MainGui)
        self.button_start_record.setGeometry(QtCore.QRect(10, 380, 100, 30))
        self.button_start_record.setObjectName("button_start_record")
        self.button_stop_record = QtWidgets.QPushButton(MainGui)
        self.button_stop_record.setGeometry(QtCore.QRect(120, 380, 100, 30))
        self.button_stop_record.setObjectName("button_stop_record")
        self.button_manual_gimbal_right = QtWidgets.QPushButton(MainGui)
        self.button_manual_gimbal_right.setGeometry(QtCore.QRect(610, 420, 41, 41))
        self.button_manual_gimbal_right.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../res/button_manual_gimbal_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_manual_gimbal_right.setIcon(icon)
        self.button_manual_gimbal_right.setObjectName("button_manual_gimbal_right")
        self.button_manual_gimbal_left = QtWidgets.QPushButton(MainGui)
        self.button_manual_gimbal_left.setGeometry(QtCore.QRect(570, 420, 41, 41))
        self.button_manual_gimbal_left.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../res/button_manual_gimbal_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_manual_gimbal_left.setIcon(icon1)
        self.button_manual_gimbal_left.setObjectName("button_manual_gimbal_left")
        self.button_manual_gimbal_down = QtWidgets.QPushButton(MainGui)
        self.button_manual_gimbal_down.setGeometry(QtCore.QRect(590, 460, 41, 41))
        self.button_manual_gimbal_down.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../res/button_manual_gimbal_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_manual_gimbal_down.setIcon(icon2)
        self.button_manual_gimbal_down.setObjectName("button_manual_gimbal_down")
        self.button_manual_gimbal_up = QtWidgets.QPushButton(MainGui)
        self.button_manual_gimbal_up.setGeometry(QtCore.QRect(590, 380, 41, 41))
        self.button_manual_gimbal_up.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../res/button_manual_gimbal_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_manual_gimbal_up.setIcon(icon3)
        self.button_manual_gimbal_up.setObjectName("button_manual_gimbal_up")
        self.combobox_preview_camera_index = QtWidgets.QComboBox(MainGui)
        self.combobox_preview_camera_index.setGeometry(QtCore.QRect(230, 420, 51, 31))
        self.combobox_preview_camera_index.setObjectName("combobox_preview_camera_index")
        self.combobox_preview_camera_index_2 = QtWidgets.QComboBox(MainGui)
        self.combobox_preview_camera_index_2.setGeometry(QtCore.QRect(230, 460, 51, 31))
        self.combobox_preview_camera_index_2.setObjectName("combobox_preview_camera_index_2")

        self.retranslateUi(MainGui)
        QtCore.QMetaObject.connectSlotsByName(MainGui)

    def retranslateUi(self, MainGui):
        _translate = QtCore.QCoreApplication.translate
        MainGui.setWindowTitle(_translate("MainGui", "Form"))
        self.button_start_preview.setText(_translate("MainGui", "Start Preview"))
        self.button_stop_preview.setText(_translate("MainGui", "Stop Preview"))
        self.button_start_tracking.setText(_translate("MainGui", "Start Tracking"))
        self.button_stop_tracking.setText(_translate("MainGui", "Stop Tracking"))
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

