'''
Created on Apr 5, 2016

@author: Rykath
Package: UI_Tk_old

Usage: functions for Laboratory/Viewer/Pattern creator
'''
from functools import partial
import tkinter as tk

import Main.settings as Settings
import Main.utilities as Utils
import Main.Engine.base as Engine
import Main.Engine.compute as Compute
import Main.Data.internal as Data
import UI_Tk_old.config as config

class GUILab():
    key = 'lab'
    name = 'Pattern-Laboratory'
    posControl = 1 #row-position in control-section
    
    def __init__(self, core, parent):
        self.core = core
        self.parent = parent
        self.wrtDetails = False #whether details were created already or not
        
    def ShowDetails(self,destroy=False):
        #destroy=True : other elements in details deleted instead of hidden
        if destroy:
            self.parent.details.content.clear()
            for i in self.parent.child:
                self.parent.child[i].wrtDetails = False
        for i in self.parent.details.content:
            for ii in self.parent.details.content[i]:
                ii.grid_remove()
        if self.wrtDetails:
            for i in range(len(self.parent.details.content[self.key])):
                self.parent.details.content[self.key][i].grid(row=i,column=0,sticky='nsew',padx=1,pady=1)
        else:
            self.parent.details.content[self.key] = []
            self.CreateWidgets(self.parent.details.content[self.key])
            self.wrtDetails = True
            
######################### OLD
def createWidgets(frame):
    #frame: GUI.lab
    size = config.LCsize
    frame.menubar = tk.Menu(frame)
    frame.menubar.cmd = tk.Menu(frame)
    frame.menubar.cmd.rot = tk.Menu(frame)
    frame.menubar.cmd.mir = tk.Menu(frame)
    frame.menubar.cmd.exp = tk.Menu(frame)
    frame.menubar.cmd.ret = tk.Menu(frame)
    frame.menubar.cmd.mov = tk.Menu(frame)
    frame.menubar.add_command(label='close',command=frame.destroy)
    frame.menubar.add_cascade(label='command',menu=frame.menubar.cmd)
    frame.menubar.cmd.add_command(label='tick & center',command=partial(cmdTick,frame))
    frame.menubar.cmd.add_command(label='next state',command=partial(cmdState,frame.parent,1))
    frame.menubar.cmd.add_command(label='previous state',command=partial(cmdState,frame.parent,-1))
    frame.menubar.cmd.add_cascade(label='rotate',menu=frame.menubar.cmd.rot)
    frame.menubar.cmd.rot.add_command(label='rotate clock-wise'         ,command=partial(cmdRotate,frame.parent,'cw'))
    frame.menubar.cmd.rot.add_command(label='rotate counter-clock-wise' ,command=partial(cmdRotate,frame.parent,'ccw'))
    frame.menubar.cmd.add_cascade(label='mirror',menu=frame.menubar.cmd.mir)
    frame.menubar.cmd.mir.add_command(label='mirror horizontal' ,command=partial(cmdMirror,frame.parent,'x'))
    frame.menubar.cmd.mir.add_command(label='mirror vertical'   ,command=partial(cmdMirror,frame.parent,'y'))
    frame.menubar.cmd.add_cascade(label='expand',menu=frame.menubar.cmd.exp)
    frame.menubar.cmd.exp.add_command(label='left'  ,command=partial(cmdMove,frame.parent,Utils.Border(left=1)))
    frame.menubar.cmd.exp.add_command(label='right' ,command=partial(cmdMove,frame.parent,Utils.Border(right=1)))
    frame.menubar.cmd.exp.add_command(label='up'    ,command=partial(cmdMove,frame.parent,Utils.Border(up=1)))
    frame.menubar.cmd.exp.add_command(label='down'  ,command=partial(cmdMove,frame.parent,Utils.Border(down=1)))
    frame.menubar.cmd.exp.add_command(label='all sides',command=partial(cmdMove,frame.parent,Utils.Border(four=1)))
    frame.menubar.cmd.add_cascade(label='retract',menu=frame.menubar.cmd.ret)
    frame.menubar.cmd.ret.add_command(label='left'  ,command=partial(cmdMove,frame.parent,Utils.Border(left=-1)))
    frame.menubar.cmd.ret.add_command(label='right' ,command=partial(cmdMove,frame.parent,Utils.Border(right=-1)))
    frame.menubar.cmd.ret.add_command(label='up'    ,command=partial(cmdMove,frame.parent,Utils.Border(up=-1)))
    frame.menubar.cmd.ret.add_command(label='down'  ,command=partial(cmdMove,frame.parent,Utils.Border(down=-1)))
    frame.menubar.cmd.ret.add_command(label='all sides',command=partial(cmdMove,frame.parent,Utils.Border(four=-1)))
    frame.menubar.cmd.ret.add_command(label='full shrink',command=partial(cmdResize,frame.parent,Utils.Border(four=0)))
    frame.menubar.cmd.add_cascade(label='move',menu=frame.menubar.cmd.mov)
    frame.menubar.cmd.mov.add_command(label='left'  ,command=partial(cmdMove,frame.parent,Utils.Border(left=-1,right=1)))
    frame.menubar.cmd.mov.add_command(label='right' ,command=partial(cmdMove,frame.parent,Utils.Border(right=-1,left=1)))
    frame.menubar.cmd.mov.add_command(label='up'    ,command=partial(cmdMove,frame.parent,Utils.Border(up=-1,down=1)))
    frame.menubar.cmd.mov.add_command(label='down'  ,command=partial(cmdMove,frame.parent,Utils.Border(down=-1,up=1)))
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
    for y in range(frame.Bdimension[1]):
        for x in range(frame.Bdimension[0]):
            if frame.data[y][x] == 1:
                frame.board[y][x].config(bg=config.LCaBgCol,fg=config.LCaFgCol,activebackground=config.LCaBgCol,activeforeground=config.LCaFgCol)
            elif frame.count[y][x] > 0:
                frame.board[y][x].config(bg=config.LCbBgCol,fg=config.LCbFgCol,activebackground=config.LCbBgCol,activeforeground=config.LCbFgCol)
            else:
                frame.board[y][x].config(bg=config.LCdBgCol,fg=config.LCdFgCol,activebackground=config.LCdBgCol,activeforeground=config.LCdFgCol)
            frame.board[y][x].config(text=frame.count[y][x])

def redrawGrid(frame):
    #frame: GUI
    width = frame.lab.Bborder.width
    height = frame.lab.Bborder.height
    if frame.core.Lcp != None:
        width += frame.core.Lcp.widthT 
        height += frame.core.Lcp.heightT
    if width > frame.lab.Bdimension[0]:
        for y in range(frame.lab.Bdimension[1]):
            for x in range(frame.lab.Bdimension[0],width):
                if x >= len(frame.lab.board[y]):
                    frame.lab.board[y].append(tk.Button(frame.lab,bg='white',width=config.LCsize,height=config.LCsize,padx=2,pady=0,command=partial(cellClicked,frame.lab,x,y)))
                if y < height:
                    frame.lab.board[y][x].grid(row=y,column=x,padx=0,pady=0)
    elif width < frame.lab.Bdimension[0]:
        for y in range(frame.lab.Bdimension[1]):
            for x in range(width,frame.lab.Bdimension[0]):
                frame.lab.board[y][x].grid_remove()
    if height > frame.lab.Bdimension[1]:
        for y in range(frame.lab.Bdimension[1],height):
            if y >= len(frame.lab.board):
                frame.lab.board.append([])
                for x in range(width):
                    frame.lab.board[y].append(tk.Button(frame.lab,bg='white',width=config.LCsize,height=config.LCsize,padx=2,pady=0,command=partial(cellClicked,frame.lab,x,y)))
            for x in range(width):
                frame.lab.board[y][x].grid(row=y,column=x,padx=0,pady=0)
    elif height < frame.lab.Bdimension[1]:
        for y in range(height,frame.lab.Bdimension[1]):
            for x in range(width):
                frame.lab.board[y][x].grid_remove()
    frame.lab.Bdimension = [width,height]
    frame.lab.data,frame.lab.count = Engine.Extend(frame.lab.Bborder,frame.core.Lcp.data[frame.lab.active],frame.core.Lcp.count[frame.lab.active])
    frame.lab.data,frame.lab.count = Engine.Extend(Utils.Border(dimension=[frame.core.Lcp.widthT,frame.core.Lcp.heightT]).add(dimension=[frame.core.Lcp.widthA[frame.lab.active],frame.core.Lcp.heightA[frame.lab.active]],invert=True),frame.lab.data,frame.lab.count)
    updateGrid(frame.lab) 

def cmdTick(frame):
    #frame: GUI.lab
    frame.data,frame.count,_ = Engine.Tick(frame.data,frame.count)
    redrawGrid(frame.parent)
   
def cmdRotate(frame,direction):
    #frame: GUI
    Compute.rotate(frame.core.Lcp,direction)
    updateLab(frame)

def cmdMirror(frame,direction):
    #frame: GUI
    Compute.mirror(frame.core.Lcp,direction)
    updateLab(frame)

def cmdResize(frame,border):
    #frame: GUI
    Compute.resize(frame,border)
    redrawGrid(frame)

def cmdMove(frame,border):
    #frame: GUI
    Compute.move(frame,border)
    redrawGrid(frame)

def cmdState(frame,amount):
    #frame: GUI
    frame.lab.active += amount
    while frame.lab.active >= frame.core.Lcp.period:
        frame.lab.active -= frame.core.Lcp.period
    while frame.lab.active < 0:
        frame.lab.active += frame.core.Lcp.period
    updateLab(frame)
    
def updateLab(frame):
    #frame: GUI
    redrawGrid(frame)
    del frame.details.content[:]
    #offset-top: 2 rows
    #width: 2 columns
    #down to: row 8
    frame.details.content.append(tk.Label(frame.details,text='Full-ID: '+str(frame.core.Lcp.ID),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=2,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Type: '+frame.core.Lcp.type,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=3,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Type-ID: '+str(frame.core.Lcp.num),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=3,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Name: '+frame.core.Lcp.name,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=4,column=0,sticky='nsew',padx=1,pady=1,columnspan=2)
    frame.details.content.append(tk.Label(frame.details,text='Period: '+str(frame.core.Lcp.period),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=5,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Live Cells: '+str(frame.core.Lcp.dataNum[frame.lab.active]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=6,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Bounding Box: '+str(frame.core.Lcp.countNum[frame.lab.active]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=6,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Height: '+str(frame.core.Lcp.heightT),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=7,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Width: '+str(frame.core.Lcp.widthT),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=7,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Speed-X: '+str(frame.core.Lcp.speed[0]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=8,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Speed-Y: '+str(frame.core.Lcp.speed[1]),bg=config.MDlblCol))
    frame.details.content[-1].grid(row=8,column=1,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Author: '+frame.core.Lcp.author,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=9,column=0,sticky='nsew',padx=1,pady=1)
    frame.details.content.append(tk.Label(frame.details,text='Committer: '+frame.core.Lcp.committer,bg=config.MDlblCol))
    frame.details.content[-1].grid(row=9,column=1,sticky='nsew',padx=1,pady=1)

def compute(frame):
    #frame: GUI
    test = False
    data,_ = Engine.Resize(frame.lab.data)
    for i in frame.core.Ddb:
        if data in i.data:
            test = True
            active = frame.core.Ddb.index(i)
    if test == False:
        frame.core.Ddb.append(Data.Pattern(len(frame.core.Ddb),Settings.user))
        frame.core.Ddb[-1].compute(frame.lab.data,frame.lab.count)
        active = -1
    frame.core.Lcp = frame.core.Ddb[active]
    frame.lab.active = frame.core.Lcp.period -1
        
    updateLab(frame)