global remoteObj

def pressUp():
    remoteObj.setKey(7)

def pressDown():
    remoteObj.setKey(8)

def pressLeft():
    remoteObj.setKey(9)

def pressRight():
    remoteObj.setKey(10)

def pressAuto():
    remoteObj.setKey(11)

def pressBlank():
    remoteObj.setKey(12)

def pressBack():
    remoteObj.setKey(13)

def pressExit():
    remoteObj.setKey(14)

def pressOk():
    remoteObj.setKey(15)

def pressSettings():
    remoteObj.setKey(16)

def pressQMenu():
    remoteObj.setKey(17)

def settingsMenu(mainMenu,remObj):
    global remoteObj
    remoteObj = remObj
    options = [("Up",pressUp),
               ("Down",pressDown),
               ("Left",pressLeft),
               ("Right",pressRight),
               ("Auto",pressAuto),
               ("Blank",pressBlank),
               ("Back",pressBack),
               ("Exit",pressExit),
               ("Ok",pressOk),
               ("Settings",pressSettings),
               ("Q.Menu",pressQMenu),
               ("Exit",mainMenu.settingsMenu.close)]
    mainMenu.settingsMenu.set_options(options)
