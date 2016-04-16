'''
Created on Apr 5, 2016

@author: Rykath
Package: UI_Tk

Usage: functions for Laboratory/Viewer/Pattern creator
'''
from functools import partial
import Tkinter as tk

import E_std.__init__ as Engine
import UI_Tk.config as config

def createWidgets(frame):
    size = config.LCsize
    frame.menubar = tk.Menu(frame)
    frame.menubar.add_command(label='close',command=frame.destroy)
    frame.config(menu=frame.menubar)
    frame.board = []
    frame.data = []
    for y in range(config.LBheight):
        frame.board.append([])
        frame.data.append([])
        for x in range(config.LBwidth):
            frame.board[y].append(tk.Button(frame,bg='white',width=size,height=size,padx=2,pady=0,command=partial(cellClicked,frame,x,y)))
            frame.board[y][x].grid(row=y,column=x,padx=0,pady=0)
            frame.data[y].append(0)

def createDetails(frame):
    del frame.details.content[:]
    frame.details.content.append(tk.Button(frame.details,text='tick',bg='white',height=0,width=0,command=partial(tick,frame.lab)))
    frame.details.content[0].grid(row=0,column=0,sticky='nsew',padx=1,pady=1)

def cellClicked(frame,x,y):
    if frame.data[y][x] == 0:
        frame.data[y][x] = 1
    else:
        frame.data[y][x] = 0
    frame.count = Engine.Count(frame.data)
    updateGrid(frame)

def updateGrid(frame):
    for y in range(len(frame.board)):
        for x in range(len(frame.board[y])):
            if frame.data[y][x] == 0:
                frame.board[y][x].config(bg='white',fg='black')
            else:
                frame.board[y][x].config(bg='black',fg='white')
            frame.board[y][x].config(text=frame.count[y][x])

def tick(frame):
    frame.data,frame.count = Engine.Tick([config.LBheight,config.LBwidth],frame.data,frame.count)
    updateGrid(frame)