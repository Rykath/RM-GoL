'''
Created on Apr 3, 2016

@author: Rykath
Package: UI_Tk

Usage: Main file for Tkinter-based Graphical-User-Interface
'''

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
        
        self.menubar = tk.Frame(self, background='grey',   width=config.Mwidth, height=config.Mheight)
        self.control = tk.Frame(self, background='black', width=config.Cwidth, height=config.Cheight)
        self.details = tk.Frame(self, background='white', width=config.Dwidth, height=config.Dheight)
        #self.lab
        
        self.menubar.grid(row=0, column=0, sticky='nsew', columnspan=2)
        self.control.grid(row=1, column=0, sticky='nsew')
        self.details.grid(row=1, column=1, sticky='nsew')
        
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        #menubar
        self.menubar.sections = []
        self.menubar.sections.append(tk.Button(self.menubar,text='quit',bg='white',command=self.quit))
        self.menubar.sections[-1].grid(row=0, column=0, sticky='ns', padx=2, pady=2)
        #control
        self.control.sections = []
        self.control.sections.append(tk.Button(self.control,text='Pattern-Laboratory',bg='white',command=self.lab))
        self.control.sections[-1].grid(row=0, column=0, sticky='nw', padx=2, pady=2)
    
    def lab(self):
        self.lab = tk.Toplevel()
        self.lab.wm_title('Laboratory')
        self.lab.parent = self
        lab.createWidgets(self.lab)
        lab.updateGrid(self.lab,self.lab.data)
    
    
        
