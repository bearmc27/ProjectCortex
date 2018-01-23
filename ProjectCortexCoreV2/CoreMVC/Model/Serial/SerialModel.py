import serial
import serial.tools.list_ports


class SerialModel:
    @staticmethod
    def get_available_serial_ports_list():
        return list(serial.tools.list_ports.comports())
