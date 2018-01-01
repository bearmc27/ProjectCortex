import sys

from GUI.MainGUI import MainGUI, QApplication


class GUI_Controller():
    # Create GUI window
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()

    @staticmethod
    def get_app():
        return GUI_Controller.app

    @staticmethod
    def change_text(new_text):
        print(new_text)
        GUI_Controller.window.change_text(new_text = new_text)
