import serial
ser = serial.Serial('/dev/tty.usbmodem14101',baudrate=9600,timeout=1)
def getValue():
    ser.write(b'g')
    arduino_data=ser.readline().decode('ascii')
    return arduino_data
while (1):
    # arduino_data = ser.readline().decode('ascii')
    # print((arduino_data))
    userInput=input('Get dta point?')
    if userInput=='y':
        print(getValue())
