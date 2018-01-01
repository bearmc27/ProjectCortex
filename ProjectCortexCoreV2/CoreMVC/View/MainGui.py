# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainGui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainGui(object):
    def setupUi(self, MainGui):
        MainGui.setObjectName("MainGui")
        MainGui.resize(600, 500)
        self.Button_StartVideo = QtWidgets.QPushButton(MainGui)
        self.Button_StartVideo.setGeometry(QtCore.QRect(10, 460, 100, 30))
        self.Button_StartVideo.setObjectName("Button_StartVideo")
        self.Button_StopVideo = QtWidgets.QPushButton(MainGui)
        self.Button_StopVideo.setGeometry(QtCore.QRect(120, 460, 100, 30))
        self.Button_StopVideo.setObjectName("Button_StopVideo")
        self.Label_Video = QtWidgets.QLabel(MainGui)
        self.Label_Video.setGeometry(QtCore.QRect(10, 10, 360, 270))
        self.Label_Video.setText("")
        self.Label_Video.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Label_Video.setObjectName("Label_Video")

        self.retranslateUi(MainGui)
        QtCore.QMetaObject.connectSlotsByName(MainGui)

    def retranslateUi(self, MainGui):
        _translate = QtCore.QCoreApplication.translate
        MainGui.setWindowTitle(_translate("MainGui", "Form"))
        self.Button_StartVideo.setText(_translate("MainGui", "Start Video"))
        self.Button_StopVideo.setText(_translate("MainGui", "Stop Video"))


# Only for testing
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainGui = QtWidgets.QWidget()
    ui = Ui_MainGui()
    ui.setupUi(MainGui)
    MainGui.show()
    sys.exit(app.exec_())
