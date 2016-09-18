'''
Created on Sep 18, 2016

@author: Rykath
Package: Main.Interface

Usage: laboratory related tkinter-functions for the UI
'''

#import tkinter as Tk
import Main.settings as Settings

def update(frame,board,boardL,boardC):
    for x in range(Settings.labSize[0]):
        for y in range(Settings.labSize[1]):
            text = boardC.get([x,y])
            bg = [Settings.cellColD,Settings.cellColL][boardL.get([x,y])]
            fg = [Settings.cellFColD,Settings.cellFColL][boardL.get([x,y])]
            board.get([x,y]).config(text=text,bg=bg,fg=fg)
            board.get([x,y]).grid(row=y,column=x)
    frame.update()