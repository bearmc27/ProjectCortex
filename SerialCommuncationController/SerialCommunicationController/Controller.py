import serial

def main():
    ser = serial.Serial()
    ser.baudrate = 57600
    ser.port = 'COM4'
    

if __name__ == '__main__':
    main()