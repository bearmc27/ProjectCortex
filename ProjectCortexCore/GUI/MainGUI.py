import sys

from PyQt5.QtWidgets import *
from GUI.Pyqt5MainGUI import Ui_MainGUI

class MainGUI(QDialog):
    def __init__(self):
        super().__init__()
        self.gui=Ui_MainGUI()
        self.gui.setupUi(self)

    def change_text(self,new_text):
        self.gui.Button_StartVideo.setText(new_text)