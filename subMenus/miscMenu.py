global remoteObj

def pressStill():
    remoteObj.setKey(18)

def pressRatio():
    remoteObj.setKey(19)

def pressUSB():
    remoteObj.setKey(20)

def pressHelp():
    remoteObj.setKey(21)

def pressKeySUp():
    remoteObj.setKey(22)

def pressKeySDown():
    remoteObj.setKey(23)

def pressRed():
    remoteObj.setKey(29)

def pressGreen():
    remoteObj.setKey(30)

def pressYellow():
    remoteObj.setKey(31)

def pressBlue():
    remoteObj.setKey(32)


def miscMenu(mainMenu,remObj):
    global remoteObj
    remoteObj = remObj
    options = [("Still",pressStill),
               ("Ratio",pressRatio),
               ("USB",pressUSB),
               ("Help",pressHelp),
               ("KeySUp",pressKeySUp),
               ("KeySDown",pressKeySDown),
               ("Red",pressRed),
               ("Green",pressGreen),
               ("Yellow",pressYellow),
               ("Blue",pressBlue),
               ("Exit",mainMenu.miscMenu.close)]
    mainMenu.miscMenu.set_options(options)
