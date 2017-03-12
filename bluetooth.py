#!/usr/bin/python
import sys
import csv
import serial
import os
from itertools import izip
from ctypes import *
from struct import pack, unpack
import struct
import binascii

# Test_branch changes
# Test_bracnh changes 2
# add  string
t = 0

f = open('/home/kalach/workfile.csv', 'wb')
ser = serial.Serial('/dev/rfcomm0', timeout = 5)

x = ser.read(10)    # before start need to reed this MARK BUTN

def readData(t):
    x = ser.read(9)  # ECG DATA 
    s = ord(ser.read(1))    # younger byte size of data 
    e = ord(ser.read(1))    # elder byte size of data 
    
    data_size = (s + e*256) - 10 # 10 - size of header
    
    print data_size
    x = ser.read(8)             # pass header chunk
    
    for i in range(0, data_size / 2):
        s = ser.read(1)
        e = ser.read(1)
        Voltage = [unpack('B', s)[0] + unpack('b',e)[0] * 256]
        temp = [t + 1]
        #print Voltage
        writer = csv.writer(f,delimiter='\t',lineterminator='\n',)
        writer.writerows(izip(temp, Voltage))
        t = temp[0]
    x = ser.read(2)             # pass \r\n
   
    return temp[0]
  
for i in range(0, 50):
    t = readData(t)

f.close()
ser.close()
