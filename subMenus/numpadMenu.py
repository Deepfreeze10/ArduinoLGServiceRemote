global remoteObj

def pressKey0():
    remoteObj.setKey(33)

def pressKey1():
    remoteObj.setKey(34)

def pressKey2():
    remoteObj.setKey(35)

def pressKey3():
    remoteObj.setKey(36)

def pressKey4():
    remoteObj.setKey(37)

def pressKey5():
    remoteObj.setKey(38)

def pressKey6():
    remoteObj.setKey(39)

def pressKey7():
    remoteObj.setKey(40)

def pressKey8():
    remoteObj.setKey(41)

def pressKey9():
    remoteObj.setKey(42)

def numpadMenu(mainMenu,remObj):
    global remoteObj
    remoteObj = remObj
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
               ("Exit",mainMenu.numpadMenu.close)]
    mainMenu.numpadMenu.set_options(options)
