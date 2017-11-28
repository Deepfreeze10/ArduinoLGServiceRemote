import serial
from time import *

class LgRemote:
    def __init__(self):
        self.serialWrite = serial.Serial('COM3')

    def setKey(self,buttonInt):
        byteArray = []
        byteArray.append((buttonInt & (0xFF << (0))) >> 0) # 2 bytes buttonInt
        byteArray.append((buttonInt & (0xFF << (8))) >> 8)
        self.serialWrite.write(bytearray(byteArray))
