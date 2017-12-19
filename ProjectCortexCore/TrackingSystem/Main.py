import SerialCommunicationController.Controller as serial_controller
import time


def main():
    controller_thread = serial_controller.Controller()
    controller_thread.start()
    time.sleep(2)
    controller_thread.set_message("0001")
    time.sleep(2)
    controller_thread.stop()
    print("End of program")


if __name__ == '__main__':
    main()
