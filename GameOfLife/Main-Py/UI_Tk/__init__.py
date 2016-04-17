'''
Created on Apr 3, 2016

@author: Rykath
Package: UI_Tk

Usage: Main file for Tkinter-based Graphical-User-Interface
'''

from functools import partial
import Tkinter as tk

import UI_Tk.config as config
import UI_Tk.lab as lab

'''
UI_Tk uses a simple 2dimensional-array to store data
'''

class GUI(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.master.title('RM-GoL ControlPanel')
        self.master.resizable(width=False,height=False)
        
        self.menubar = tk.Menu(self)
        self.master.config(menu=self.menubar)
        self.control = tk.Frame(self, background='black', width=config.MCwidth, height=config.MCheight)
        self.details = tk.Frame(self, background=config.MDbgCol, width=config.MDwidth, height=config.MDheight)
        self.lab = None
        
        self.control.grid(row=0, column=0, sticky='nsew')
        self.details.grid(row=0, column=1, sticky='nsew')
        
        self.grid()
        self.createWidgets()
        
        self.db = []
    
    def createWidgets(self):
        #menubar
        self.menubar.add_command(label='quit',command=self.quit)
        #control
        self.control.sections = []
        self.control.sections.append(tk.Button(self.control,text='Pattern-Laboratory',bg='white',command=self.butLab))
        self.control.sections[-1].grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        #details
        self.details.state = None
        self.details.content = []
    
    def butLab(self):
        if self.lab == None or self.lab.winfo_exists() == 0:
            self.lab = tk.Toplevel()
            self.lab.resizable(width=False,height=False)
            self.lab.wm_title('RM-GoL Laboratory')
            self.lab.parent = self
            lab.createWidgets(self.lab)
            lab.cellClicked(self.lab,int(config.LBwidth/2),int(config.LBheight/2))
            lab.updateGrid(self.lab)
        if self.details.state != 'lab':
            self.details.state = 'lab'
            lab.createDetails(self)
        
