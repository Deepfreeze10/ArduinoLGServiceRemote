import menu ## version <3.0.3
import sys
from lgRemote import *
from subMenus.basicMenu import *
from subMenus.serviceMenu import *
from subMenus.playerMenu import *
from subMenus.numpadMenu import *
from subMenus.miscMenu import *
from subMenus.tvMenu import *
from subMenus.settingsMenu import *

mainMenu = menu.Menu(title='LG remote menu')
mainMenu.basicMenu = menu.Menu(title='LG remote basic menu')
mainMenu.serviceMenu = menu.Menu(title='LG remote service menu')
mainMenu.playerMenu = menu.Menu(title='LG remote player menu')
mainMenu.numpadMenu = menu.Menu(title='LG remote numpad menu')
mainMenu.miscMenu = menu.Menu(title='LG remote misc menu')
mainMenu.tvMenu = menu.Menu(title='LG remote tv menu')
mainMenu.settingsMenu = menu.Menu(title='LG remote settings menu')

remoteObj = LgRemote('COM3')

def setComPort():
    global remoteObj
    arduinoPort = raw_input("Input Arduino COM port [COM3]:")
    del remoteObj
    remoteObj = LgRemote(arduinoPort)

def exitFunction():
    sys.exit()

def menu():
    options = [("Set COM port",setComPort),
               ("Basic menu",mainMenu.basicMenu.open),
               ("Service menu",mainMenu.serviceMenu.open),
               ("Settings/Menu menu",mainMenu.settingsMenu.open),
               ("Numpad menu",mainMenu.numpadMenu.open),
               ("Player menu",mainMenu.playerMenu.open),
               ("TV menu",mainMenu.tvMenu.open),
               ("Misc menu",mainMenu.miscMenu.open),
               ("Exit",exitFunction)]
    mainMenu.set_options(options)

if __name__ == '__main__':
    menu()
    basicMenu(mainMenu,remoteObj)
    serviceMenu(mainMenu,remoteObj)
    settingsMenu(mainMenu,remoteObj)
    numpadMenu(mainMenu,remoteObj)
    playerMenu(mainMenu,remoteObj)
    miscMenu(mainMenu,remoteObj)
    tvMenu(mainMenu,remoteObj)
    mainMenu.open()
