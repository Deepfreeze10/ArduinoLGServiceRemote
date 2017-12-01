import serial
from time import *

class LgRemote:
    def __init__(self,port):
        self.serialWrite = serial.Serial(port,write_timeout = 1)

    def setKey(self,buttonInt):
        byteArray = []
        byteArray.append((buttonInt & (0xFF << (0))) >> 0) # 2 bytes buttonInt
        byteArray.append((buttonInt & (0xFF << (8))) >> 8)
        self.serialWrite.write(bytearray(byteArray))
        self.serialWrite.reset_output_buffer()

    def __del__(self):
        self.serialWrite.close()
