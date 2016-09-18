'''
Created on Jul 7, 2016

@author: Rykath
Package: Main.Interface

Usage: functions/content used in several modules
'''

import tkinter as Tk

def menubar(frame,content):
    frame.menu = Tk.Menu(frame)
    #frame.submenu = []
    for i in content:
        if i[0] == 'button':
            frame.menu.add_command(label=i[1],command=i[2])
    frame.config(menu=frame.menu)

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
        