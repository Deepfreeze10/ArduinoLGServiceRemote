global remoteObj

def pressTvRadio():
    remoteObj.setKey(47)

def pressGuide():
    remoteObj.setKey(48)

def pressInfo():
    remoteObj.setKey(49)

def pressAvMode():
    remoteObj.setKey(50)

def pressFav():
    remoteObj.setKey(51)

def pressList():
    remoteObj.setKey(52)

def pressText():
    remoteObj.setKey(53)

def pressRec():
    remoteObj.setKey(54)

def pressSimplink():
    remoteObj.setKey(55)


def tvMenu(mainMenu,remObj):
    global remoteObj
    remoteObj = remObj
    options = [("TV/Radio",pressTvRadio),
               ("Guide",pressGuide),
               ("Info",pressInfo),
               ("AV mode",pressAvMode),
               ("Fav",pressFav),
               ("List",pressList),
               ("Text",pressText),
               ("Rec",pressRec),
               ("Simplink",pressSimplink),
               ("Exit",mainMenu.tvMenu.close)]
    mainMenu.tvMenu.set_options(options)
