# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Pyqt5MainGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainGUI(object):
    def setupUi(self, MainGUI):
        MainGUI.setObjectName("MainGUI")
        MainGUI.resize(600, 500)
        self.Button_StartVideo = QtWidgets.QPushButton(MainGUI)
        self.Button_StartVideo.setGeometry(QtCore.QRect(10, 460, 100, 30))
        self.Button_StartVideo.setObjectName("Button_StartVideo")
        self.Button_StopVideo = QtWidgets.QPushButton(MainGUI)
        self.Button_StopVideo.setGeometry(QtCore.QRect(120, 460, 100, 30))
        self.Button_StopVideo.setObjectName("Button_StopVideo")
        self.Label_Video = QtWidgets.QLabel(MainGUI)
        self.Label_Video.setGeometry(QtCore.QRect(10, 10, 360, 270))
        self.Label_Video.setText("")
        self.Label_Video.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Label_Video.setObjectName("Label_Video")

        self.retranslateUi(MainGUI)
        QtCore.QMetaObject.connectSlotsByName(MainGUI)

    def retranslateUi(self, MainGUI):
        _translate = QtCore.QCoreApplication.translate
        MainGUI.setWindowTitle(_translate("MainGUI", "Form"))
        self.Button_StartVideo.setText(_translate("MainGUI", "Start Video"))
        self.Button_StopVideo.setText(_translate("MainGUI", "Stop Video"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainGUI = QtWidgets.QWidget()
    ui = Ui_MainGUI()
    ui.setupUi(MainGUI)
    MainGUI.show()
    sys.exit(app.exec_())
