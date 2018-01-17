import serial


class SerialConnection:
    def __init__(self, baudrate, port):
        self.port = port
        self.baudrate = baudrate

        self.ser = serial.Serial()
        self.ser.baudrate = self.baudrate
        self.ser.port = self.port
        self.ser.open()

    def set_baudrate(self, baudrate):
        self.baudrate = baudrate
        self.ser.baudrate = self.baudrate

    def set_port(self, port):
        self.port = port
        self.ser.port = self.port

    def get_baudrate(self):
        return self.baudrate

    def get_port(self):
        return self.port

    def close_serial(self):
        print("Close Serial")
        self.ser.close()

    def is_serial_open(self):
        return self.ser.isOpen()

    def send_serial_message(self, message):
        # Write message to serial bus
        # Encode message from string to byte
        self.ser.write(message.encode())
