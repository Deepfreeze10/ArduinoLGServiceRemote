import menu
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
from lgRemote import *

mainMenu = menu.Menu(title='LG remote menu')

remoteObj = LgRemote()

def pressKey0():
    remoteObj.setKey(0)

def pressKey1():
    remoteObj.setKey(1)

def pressKey2():
    remoteObj.setKey(2)

def pressKey3():
    remoteObj.setKey(3)

def pressKey4():
    remoteObj.setKey(4)

def pressKey5():
    remoteObj.setKey(5)

def pressKey6():
    remoteObj.setKey(6)

def pressKey7():
    remoteObj.setKey(7)

def pressKey8():
    remoteObj.setKey(8)

def pressKey9():
    remoteObj.setKey(9)

def pressEzAdjust():
    remoteObj.setKey(10)

def pressInStart():
    remoteObj.setKey(11)

def exitFunction():
    sys.exit()

def menu():
    options = [("1",pressKey1),
               ("2",pressKey2),
               ("3",pressKey3),
               ("4",pressKey4),
               ("5",pressKey5),
               ("6",pressKey6),
               ("7",pressKey7),
               ("8",pressKey8),
               ("9",pressKey9),
               ("0",pressKey0),
               ("ezAdjust",pressEzAdjust),
               ("inStart",pressInStart),
               ("Exit",exitFunction)]
    mainMenu.set_options(options)

if __name__ == '__main__':
    menu()
    mainMenu.open()
