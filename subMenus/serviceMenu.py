global remoteObj

def pressEzAdjust():
    remoteObj.setKey(44)

def pressInStart():
    remoteObj.setKey(43)

def pressInStop():
    remoteObj.setKey(45)

def pressPowerOnly():
    remoteObj.setKey(46)

def pressPowerOnlyPass():
    remoteObj.setKey(57)

def pressServicePass():
    remoteObj.setKey(56)

def serviceMenu(mainMenu,remObj):
    global remoteObj
    remoteObj = remObj
    options = [("EzAdjust",pressEzAdjust),
               ("InStart",pressInStart),
               ("InStop",pressInStop),
               ("PowerOnly",pressPowerOnly),
               ("PowerOnly Pass",pressPowerOnlyPass),
               ("Service Pass",pressServicePass),
               ("Exit",mainMenu.serviceMenu.close)]
    mainMenu.serviceMenu.set_options(options)
