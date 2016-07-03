'''
Created on Jun 22, 2016

@author: Rykath
Package: Main

Executing Module
'''

def runMain():
    import tkinter
    
    import Main.core
    import Main.settings
    import Main.Interface.database as UI_db
    
    core = Main.core.Core()
    running = True
    
    obj = UI_db.UI_patternviewer(Main.settings.gui)
    core.ui[obj.key] = obj
    
    for k in core.ui.keys():
        core.ui[k].create()
    while running:
        running = False
        for k in core.ui.keys():
            try:
                core.ui['db-pv'].update()
            except(tkinter.TclError):
                pass
            else:
                running = True

if __name__ == '__main__':
    runMain()