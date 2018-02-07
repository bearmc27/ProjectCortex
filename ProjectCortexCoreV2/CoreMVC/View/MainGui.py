from PyQt5 import QtWidgets

from CoreMVC.View.Template_MainGui import Ui_MainGui


class MainGui(QtWidgets.QWidget, Ui_MainGui):
    """
    Actual MainGui class
    """

    def __init__(self, controller, parent=None):
        super().__init__(parent=parent)
        self.controller = controller
        self.setupUi(self)

    def closeEvent(self, QCloseEvent):
        self.controller.main_gui_closeEvent()
