'''
Created on Apr 5, 2016

@author: Rykath
Package: UI_Tk

Usage: functions for Laboratory/Viewer/Pattern creator
'''
from functools import partial
import Tkinter as tk

import Main.settings as Settings
import E_std.__init__ as Engine
import Data.internal as Data
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
    frame.details.content.append(tk.Button(frame.details,text='tick & center',bg=config.MDbutCol,height=0,width=0,command=partial(tick,frame.lab)))
    frame.details.content[-1].grid(row=0,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Button(frame.details,text='compute',bg=config.MDbutSCol,height=0,width=0,command=partial(compute,frame)))
    frame.details.content[-1].grid(row=1,column=0,columnspan=2,sticky='nsew',padx=1,pady=1)

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
    frame.data,frame.count,_ = Engine.Tick(frame.data,frame.count,[config.LBheight,config.LBwidth])
    updateGrid(frame)

def compute(frame):
    test = False
    data,_ = Engine.Resize(frame.lab.data)
    for i in frame.db:
        #print(data,i.data)
        if data in i.data:
            test = True
    if test == False:
        frame.db.append(Data.Pattern(len(frame.db),Settings.user))
        frame.db[-1].compute(frame.lab.data,frame.lab.count)
    frame.details.content.append(tk.Label(frame.details,text='Full-ID: '+str(frame.db[-1].ID),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=2,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Type: '+frame.db[-1].type,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=3,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Type-ID: '+str(frame.db[-1].num),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=3,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Name: '+frame.db[-1].name,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=4,column=0,sticky='nsew',padx=1,pady=1,columnspan=2)
    frame.details.content.append(tk.Label(frame.details,text='Period: '+str(frame.db[-1].period),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=5,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Live Cells: '+str(frame.db[-1].dataNum),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=6,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Bounding Box: '+str(frame.db[-1].countNum),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=6,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Author: '+frame.db[-1].author,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=7,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Committer: '+frame.db[-1].committer,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=7,column=1,sticky='nsew',padx=1,pady=1)