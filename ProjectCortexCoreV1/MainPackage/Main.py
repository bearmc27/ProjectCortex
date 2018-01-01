from __future__ import print_function

# from TrackingSystem import TrackingSystem as tracking_sys
import sys

from PyQt5.QtWidgets import QApplication

from GUI.Controller import GUI_Controller

"""
Objective:
- Kick-starting the program.
- Read configuration file and pass it to other class
"""


def main():
    # tracking_system = tracking_sys.TrackingSystem()

    gui_controller = GUI_Controller()
    GUI_Controller.change_text(new_text = "HAHA")

    sys.exit(GUI_Controller.get_app().exec())


if __name__ == '__main__':
    main()
