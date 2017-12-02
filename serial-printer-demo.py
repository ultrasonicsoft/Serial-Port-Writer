#!/usr/bin/python
import sys
import time
import serial

def sendDataOverSerialPort(data):
    ser = serial.Serial(port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

    print('[serialPrinter]: Trying to send data over serial port...')

    if ser.isOpen():
        try:
            ser.flushInput()
            ser.flushOutput()
            ser.write(bytes(data,'iso-8859-1'))
            print('[serialPrinter]: Data sent successfully!')
        except Exception as e1:
            logMsg ='[serialPrinter]: Communication error...:' + str(e1)
            print(logMsg)    
   
       
if __name__ == "__main__":
    sendDataOverSerialPort("Sent from Raspi 3 to Windows 10! something else to send....")

