'''
Created on Jul 7, 2016

@author: Rykath
Package: UI_Tk

Usage: functions/content used in several modules
'''

import tkinter as Tk

def menubar(frame,content):
    frame.menu = Tk.Menu(frame)
    menubarBuild(frame,frame.menu,content)
    frame.config(menu=frame.menu)

def menubarBuild(frame,menu,content):
    # sub-function of menubar
    #! only called by menubar
    #! recursive
    submenu = []
    for i in content:
        if i[0] == 'button':
            menu.add_command(label=i[1],command=i[2])
        if i[0] == 'menu':
            submenu.append(Tk.Menu(frame))
            menubarBuild(frame,submenu[-1],i[2])
            menu.add_cascade(label=i[1],menu=submenu[-1])

def close(frame):
    frame.destroy()

def create(title):
    obj = Tk.Tk()
    obj.resizable(False,False)
    obj.title(title)
    return obj

def update(obj):
    obj.update()

def make(typ,master,text=None,command=None):
    if typ == 'button':
        return Tk.Button(master=master,text=text,command=command)
        