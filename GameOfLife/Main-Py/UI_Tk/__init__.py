'''
Created on Apr 3, 2016

@author: Rykath

Main file for Tkinter-based Graphical-User-Interface
'''

import Tkinter as tk

import UI_Tk.config as config

'''
UI_Tk uses a simple 2dimensional-array to store data
'''

class GUI(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.viewer = tk.Frame(self, background="white", width=config.Vwidth, height=config.Vheight)
        self.control = tk.Frame(self, background="black", width=config.Cwidth, height=config.Cheight)
        
        self.viewer.grid(row=0, column=0, sticky="nsew")
        self.control.grid(row=0, column=1, sticky="nsew")
        
        