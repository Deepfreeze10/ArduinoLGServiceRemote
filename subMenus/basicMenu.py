global remoteObj

def pressPower():
    remoteObj.setKey(0)

def pressMute():
    remoteObj.setKey(1)

def pressInput():
    remoteObj.setKey(2)

def pressVolPlus():
    remoteObj.setKey(3)

def pressVolMin():
    remoteObj.setKey(4)

def pressPagePlus():
    remoteObj.setKey(5)

def pressPageMin():
    remoteObj.setKey(6)

def basicMenu(mainMenu,remObj):
    global remoteObj
    remoteObj = remObj
    options = [("Power on/off",pressPower),
               ("Mute on/off",pressMute),
               ("Select input",pressInput),
               ("Volume +",pressVolPlus),
               ("Volume -",pressVolMin),
               ("Page +",pressPagePlus),
               ("Page -",pressPageMin),
               ("Exit",mainMenu.basicMenu.close)]
    mainMenu.basicMenu.set_options(options)
