global remoteObj

def pressRewind():
    remoteObj.setKey(24)

def pressFastForward():
    remoteObj.setKey(25)

def pressPlay():
    remoteObj.setKey(26)

def pressStop():
    remoteObj.setKey(27)

def pressPause():
    remoteObj.setKey(28)

def playerMenu(mainMenu,remObj):
    global remoteObj
    remoteObj = remObj
    options = [("Rewind",pressRewind),
               ("Fast Forward",pressFastForward),
               ("Play",pressPlay),
               ("Stop",pressStop),
               ("Pause",pressPause),
               ("Exit",mainMenu.playerMenu.close)]
    mainMenu.playerMenu.set_options(options)
