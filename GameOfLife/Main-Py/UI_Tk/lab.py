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
    frame.menucmd = tk.Menu(frame)
    frame.menubar.add_command(label='close',command=frame.destroy)
    frame.menubar.add_cascade(label='command',menu=frame.menucmd)
    frame.menucmd.add_command(label='tick & center',command=partial(cmdTick,frame))
    frame.menucmd.add_command(label='rotate clock-wise',command=partial(cmdRotate,frame.parent,'cw'))
    frame.menucmd.add_command(label='rotate counter-clock-wise',command=partial(cmdRotate,frame.parent,'ccw'))
    frame.menucmd.add_command(label='mirror horizontal',command=partial(cmdMirror,frame.parent,'x'))
    frame.menucmd.add_command(label='mirror vertical',command=partial(cmdMirror,frame.parent,'y'))
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
    #frame: GUI
    del frame.details.content[:]
    frame.details.content.append(tk.Button(frame.details,text='tick & center',bg=config.MDbutCol,height=0,width=0,command=partial(cmdTick,frame.lab)))
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
    #frame: GUI.lab
    for y in range(len(frame.board)):
        for x in range(len(frame.board[y])):
            if frame.data[y][x] == 0:
                frame.board[y][x].config(bg='white',fg='black')
            else:
                frame.board[y][x].config(bg='black',fg='white')
            frame.board[y][x].config(text=frame.count[y][x])

def redrawGrid(frame):
    #frame: GUI
    width = frame.lab.Bborder[0] + frame.lab.Bborder[1]
    height = frame.lab.Bborder[2] + frame.lab.Bborder[3]
    if frame.lab.active != None:
        width += frame.db[frame.lab.active].widthT 
        height += frame.db[frame.lab.active].heightT
    if width > frame.lab.Bdimension[0]:
        for y in range(len(frame.lab.board)):
            for x in range(frame.lab.Bdimension[0],width):
                frame.lab.board[y].append(tk.Button(frame.lab,bg='white',width=config.LCsize,height=config.LCsize,padx=2,pady=0,command=partial(cellClicked,frame.lab,x,y)))
                frame.lab.board[y][x].grid(row=y,column=x,padx=0,pady=0)
                frame.lab.data[y].append(0)
    elif width < frame.lab.Bdimension[0]:
        for y in range(len(frame.lab.board)):
            del frame.lab.board[y][width:]
            del frame.lab.data[y][width:]                
    if height > frame.lab.Bdimension[1]:
        for y in range(frame.lab.Bdimension[1],height):
            frame.lab.board.append([])
            frame.lab.data.append([])
            for x in range(len(frame.lab.board[0])):
                frame.lab.board[y].append(tk.Button(frame.lab,bg='white',width=config.LCsize,height=config.LCsize,padx=2,pady=0,command=partial(cellClicked,frame.lab,x,y)))
                frame.lab.board[y][x].grid(row=y,column=x,padx=0,pady=0)
                frame.lab.data[y].append(0)
    elif height < frame.lab.Bdimension[1]:
        del frame.lab.board[height:]
        del frame.lab.data[height:]
    frame.lab.Bdimension = [width,height]
    frame.lab.data,frame.lab.count = Engine.Extend(frame.lab.Bborder,frame.db[frame.lab.active].data[-1],frame.db[frame.lab.active].count[-1])
    updateGrid(frame.lab) 

def cmdTick(frame):
    frame.data,frame.count,_ = Engine.Tick(frame.data,frame.count)
    redrawGrid(frame.parent)
   
def cmdRotate(frame,direction):
    #frame: GUI
    if direction == 'cw':
        frame.db[frame.lab.active].rotate()
        frame.db[frame.lab.active].mirror(True,False)
    elif direction == 'ccw':
        frame.db[frame.lab.active].rotate()
        frame.db[frame.lab.active].mirror(False,True)
    updateLab(frame)

def cmdMirror(frame,direction):
    #frame: GUI
    if direction == 'x':
        frame.db[frame.lab.active].mirror(True,False)
    elif direction == 'y':
        frame.db[frame.lab.active].mirror(False,True)
    updateLab(frame)
    
def updateLab(frame):
    #frame: GUI
    #frame.lab.data,frame.lab.count = Engine.Extendto([config.LBwidth,config.LBheight],frame.db[frame.lab.active].data[-1],frame.db[frame.lab.active].count[-1])
    #frame.lab.data,frame.lab.count = frame.db[frame.lab.active].data[-1],frame.db[frame.lab.active].count[-1]
    redrawGrid(frame)
    del frame.details.content[:]
    #offset-top: 2 rows
    #width: 2 columns
    #down to: row 8
    frame.details.content.append(tk.Label(frame.details,text='Full-ID: '+str(frame.db[frame.lab.active].ID),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=2,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Type: '+frame.db[frame.lab.active].type,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=3,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Type-ID: '+str(frame.db[frame.lab.active].num),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=3,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Name: '+frame.db[frame.lab.active].name,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=4,column=0,sticky='nsew',padx=1,pady=1,columnspan=2)
    frame.details.content.append(tk.Label(frame.details,text='Period: '+str(frame.db[frame.lab.active].period),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=5,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Live Cells: '+str(frame.db[frame.lab.active].dataNum[0]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=6,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Bounding Box: '+str(frame.db[frame.lab.active].countNum[0]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=6,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Height: '+str(frame.db[frame.lab.active].heightT),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=7,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Width: '+str(frame.db[frame.lab.active].widthT),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=7,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Speed-X: '+str(frame.db[frame.lab.active].speed[0]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=8,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Speed-Y: '+str(frame.db[frame.lab.active].speed[1]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=8,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Author: '+frame.db[frame.lab.active].author,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=9,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Committer: '+frame.db[frame.lab.active].committer,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=9,column=1,sticky='nsew',padx=1,pady=1)

def compute(frame):
    #frame: GUI
    test = False
    data,_ = Engine.Resize(frame.lab.data)
    for i in frame.db:
        if data in i.data:
            test = True
            frame.lab.active = frame.db.index(i)
    if test == False:
        frame.db.append(Data.Pattern(len(frame.db),Settings.user))
        frame.db[-1].compute(frame.lab.data,frame.lab.count)
        frame.lab.active = -1
    updateLab(frame)