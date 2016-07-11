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

lines = []
t = 0

f = open('/home/kalach/workfile.csv', 'wb')
ser = serial.Serial('/dev/rfcomm0', timeout = 5)

x = ser.read(10)    # before start need to reed this MARK BUTN

def readData(t):
    x = ser.read(9) # ECG DATA 
    
    s = ord(ser.read())    # younger byte size of data 
    e = ord(ser.read())    # elder byte size of data 
    data_size = (s + e*256) - 10 # 10 - size of header
    #print "data_size = %i" %data_size
    
    x = ser.read(8)             # pass header need to 8!!!!!!!!!
    
    for i in range(0, data_size / 2):
        s = ser.read()
        e = ser.read()
        Voltage = [unpack('B', s)[0] + unpack('b',e)[0] * 256]
    
    x = ser.read(2)             # pass \r\n
   
        
    temp = [t + 1]
    writer = csv.writer(f,delimiter='\t',lineterminator='\n',)
    writer.writerows(izip(temp, Voltage))
    return temp[0]
    
for i in range(0, 60):
    t = readData(t)

    

f.close()
ser.close()
