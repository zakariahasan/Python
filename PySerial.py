import serial

se = serial.Serial("/dev/tty.usbmodem14101",buadrate=9600,timeout=1)  # to find usb on mac.CLI: ls -l /dev/cu.usb*


while True:
  arduino_data = se.readline().decode("ascii") # decode method clean up data. remove prefix "b" and endline.
  print(adduino_data)
