'''
Created on Sep 18, 2016

@author: Rykath
Package: UI_Tk

Usage: laboratory related tkinter-functions for the UI
'''

#import tkinter as Tk
import Main.settings as Settings

def update(frame,obj):
    X,Y = obj.boardMove
    for x in range(Settings.labSize[0]):
        for y in range(Settings.labSize[1]):
            text = obj.boardC.get([x+X,y+Y])
            bg = [Settings.cellColD,Settings.cellColL][obj.boardL.get([x+X,y+Y])]
            fg = [Settings.cellFColD,Settings.cellFColL][obj.boardL.get([x+X,y+Y])]
            obj.board.get([x,y]).config(text=text,bg=bg,fg=fg)
            obj.board.get([x,y]).grid(row=y,column=x)
    frame.update()