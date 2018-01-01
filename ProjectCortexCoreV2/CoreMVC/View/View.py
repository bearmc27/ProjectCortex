from PyQt5 import QtWidgets

from CoreMVC.View.MainGui import Ui_MainGui


class View():
    def __init__(self, app):
        self.app = app
        self.window_main_gui = QtWidgets.QWidget()
        self.ui_main_gui = Ui_MainGui()
        self.ui_main_gui.setupUi(self.window_main_gui)
        self.window_main_gui.show()

    def set_controller(self, controller):
        self.controller = controller
