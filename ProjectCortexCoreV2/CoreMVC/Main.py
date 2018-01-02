import sys

from PyQt5 import QtWidgets

from CoreMVC.Controller.Controller import Controller
from CoreMVC.Model.Model import Model
from CoreMVC.View.View import View


def main():
    """
    Starting program of Project Cortex

    Kick start all necessary items

    Returns:

    """

    # Create Pyqt Application
    app = QtWidgets.QApplication(sys.argv)

    # Create MVC modules
    view = View(app = app)
    model = Model()
    controller = Controller(view = view, model = model)
    view.set_controller(controller = controller)
    model.set_controller(controller = controller)
    model.set_view(view = view)

    # Create MainGui
    view.main_gui_create()

    # Setup view slots and signals
    view.main_gui_setup_ui_slots()

    # Show view window
    view.main_gui_show()

    # Run mainloop of application, system exit on application terminate
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
