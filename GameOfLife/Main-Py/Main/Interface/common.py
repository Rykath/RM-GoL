'''
Created on Jul 7, 2016

@author: Rykath
Package: Main.Interface

Usage: functions/content used in several modules
'''

from functools import partial

def menubar(obj):
    obj.menu = []
    obj.menu.append(['button','Close',partial(close,obj)])
    #obj.menubar.append(['button','Control',partial(openControl,obj)])
    obj.GUIc.menubar(obj.frame,obj.menu)

def close(obj):
    obj.GUIc.close(obj.frame)

def importGui(name):
    #imports current GUI-Package
    #name is usually: Main.settings.gui
    if name == 'tkinter':
            import UI_Tk
            UI = UI_Tk
    #elif name == 'pygame':
    #    import UI_Pg
    #    UI = UI_Pg
    return UI