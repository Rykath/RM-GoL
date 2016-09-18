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
    #import Main.Interface.database as UI_db
    import Main.Interface.laboratory as UI_lab
    
    core = Main.core.Core()
    running = True
    
    obj = UI_lab.UI_laboratory(Main.settings.gui,core)
    core.ui[obj.key] = obj
    
    while running:
        running = False
        d = []
        for k in core.ui.keys():
            try:
                core.ui[k].update()
            except(tkinter.TclError):
                d.append(k)
            else:
                running = True
        for k in d:
            del core.ui[k]

if __name__ == '__main__':
    runMain()