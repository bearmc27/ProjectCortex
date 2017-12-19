import serial
import time
from random import randint
import threading

offset = -8
current_position = 0

ONE_REVOLUTION = 4096

ser = serial.Serial()
ser.baudrate = 57600
ser.port = 'COM4'
ser.open()


def get_random_4place_integer():
    return str(randint(0, ONE_REVOLUTION)).zfill(4)


def get_new_position():
    global current_position
    global offset
    if (current_position == ONE_REVOLUTION or current_position == 0):
        offset = -offset
    current_position = current_position + offset
    return str(current_position).zfill(4)


def send_serial_message(message):
    print(message)
    ser.write(message.encode())


def main():
    while (True):
        send_serial_message(get_new_position()+";")
        time.sleep(0.005)


if __name__ == '__main__':
    main()
