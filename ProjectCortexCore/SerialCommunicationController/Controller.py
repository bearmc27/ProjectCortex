"""
Objective:
- Connect python program to Arduino through serial.
- Provide function to send message to Arduino.
"""
import serial


class Controller:
    ONE_REVOLUTION = 4096

    keep_looping = True
    refresh_rate = 0.1
    message = "000000000;"

    ser = serial.Serial()
    ser.baudrate = 57600
    ser.port = 'COM7'
    ser.open()

    # Write message to serial bus
    def send_serial_message(self, message):
        # print(msg)
        self.ser.write(message.encode())
