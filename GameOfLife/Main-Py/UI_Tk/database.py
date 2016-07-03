'''
Created on Jul 3, 2016

@author: Rykath
Package: Main.Interface

Usage: database related tkinter-functions for the UI
'''

import tkinter as Tk

def create(title):
    obj = Tk.Tk()
    obj.resizable(False,False)
    obj.title(title)
    return obj

def update(obj):
    obj.update()