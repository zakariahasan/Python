import serial
import time
ser = serial.Serial('/dev/tty.usbmodem14101',baudrate=9600,timeout=1)

time.sleep(3)
numpoint=7
dataList=[0]*numpoint

def getValue():
    ser.write(b'g')
    arduino_data=ser.readline().decode().split('\r\n')
    return arduino_data[0]
while (1):
    # arduino_data = ser.readline().decode('ascii')
    # print((arduino_data))
    userInput=input('Get dta point?')
    if userInput=='y':
        for i in range(0,numpoint):
            data=getValue()
            dataList[i]=data
        print(dataList)

