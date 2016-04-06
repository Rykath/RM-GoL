'''
Created on Apr 5, 2016

@author: Rykath
Package: UI_Tk

Usage: functions for Laboratory/Viewer/Pattern creator
'''
from functools import partial
import Tkinter as tk

def createWidgets(frame):
    size = 0
    frame.board = []
    frame.data = []
    for y in range(10):
        frame.board.append([])
        frame.data.append([])
        for x in range(10):
            frame.board[y].append(tk.Button(frame,bg='white',width=size,height=size,command=partial(cellClicked,frame,x,y)))
            frame.board[y][x].grid(row=y,column=x,padx=0,pady=0)
            frame.data[y].append(0)

def cellClicked(frame,x,y):
    if frame.data[y][x] == 0:
        frame.data[y][x] = 1
        frame.board[y][x].config(bg='black')
    else:
        frame.data[y][x] = 0
        frame.board[y][x].config(bg='white')
    updateGrid(frame,frame.data)

def updateGrid(frame,data):
    for y in range(len(frame.board)):
        for x in range(len(frame.board[y])):
            if data[y][x] == 0:
                frame.board[y][x].config(bg='white')
            else:
                frame.board[y][x].config(bg='black')