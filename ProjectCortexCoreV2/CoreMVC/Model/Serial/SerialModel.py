import serial


class SerialModel:
    def __init__(self, baudrate, port):
        self.ser = serial.Serial()
        self.ser.baudrate = baudrate
        self.ser.port = port
        # self.ser.open()

    def set_baudrate(self, baudrate):
        self.ser.baudrate = baudrate

    def set_port(self, port):
        self.ser.port = port

    def close_serial(self):
        self.ser.close()

    def is_serial_open(self):
        return self.ser.isOpen()

    def send_serial_message(self, message):
        # Write message to serial bus
        # Encode message from string to byte
        self.ser.write(message.encode())
