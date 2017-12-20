"""
Objective:
- Connect python program to Arduino through serial.
- Send new gimbal position to Arduino continuously.
"""
import serial
import time
import threading


class Controller(threading.Thread):
    ONE_REVOLUTION = 4096

    keep_looping = True
    refresh_rate = 0.1
    message = '0000'

    ser = serial.Serial()
    ser.baudrate = 57600
    ser.port = 'COM6'
    ser.open()

    def __init__(self):
        super(Controller, self).__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while (not self.stopped()):
            self.send_serial_message(self.message + ";")
            time.sleep(self.refresh_rate)

    def send_serial_message(self, msg):
        # print(msg)
        self.ser.write(msg.encode())

    def set_message(self, msg1, msg2):
        self.message = str(msg1).zfill(4) + str(msg2).zfill(4)
        print("Message is now: " + self.message)
