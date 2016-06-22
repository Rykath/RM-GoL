'''
Created on Apr 3, 2016

@author: Rykath
Package: UI_Tk

Usage: Main file for Tkinter-based Graphical-User-Interface
'''

from functools import partial
import tkinter as tk

import UI_Tk.config as config
import UI_Tk.lab as lab
import UI_Tk.viewer as viewer
import Main.utilities as Utils

'''
UI_Tk uses a simple 2dimensional-array to store data
'''

class GUI(tk.Frame):
    
    def __init__(self, core, master=None):
        tk.Frame.__init__(self, master)
        
        #-- variables
        self.core = core
        self.child = {}
        for i in [viewer.GUIViewer(self.core,self)]:
            self.child[i.key] = i
        self.mode = 'viewer' #default mode
        
        #-- main window
        self.master.title('RM-GoL ControlPanel')
        self.master.resizable(width=False,height=False)
        #-- menubar
        self.menubar = tk.Menu(self)
        self.master.config(menu=self.menubar)
        self.menubar.add_command(label='quit',command=self.quit)
        #-- control section
        self.control = tk.Frame(self, background=config.MCbgCol, width=config.MCwidth, height=config.MCheight)
        self.control.grid(row=0, column=0, sticky='nsew')
        self.control.content = [] #list with tk-elements from top to bottom
        for i in self.child:
            self.control.content.append(tk.Button(self.control,text=self.child[i].name,bg=config.MCbutBgCol,command=partial(self.cmdChangeMode,i)))
            self.control.content[-1].grid(row=self.child[i].posControl, column=0, sticky='nsew', padx=2, pady=2)
        #self.control.content.append(tk.Button(self.control,text='Pattern-Laboratory',bg='white',command=self.butLab))
        #self.control.content[-1].grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
        
        #-- details section
        self.details = tk.Frame(self, background=config.MDbgCol, width=config.MDwidth, height=config.MDheight)
        self.details.grid(row=0, column=1, sticky='nsew')
        self.details.content = {} #contains lists with tk-elements for each mode
        
        ##self.lab = None
        
        
        self.grid()
        ##self.createWidgets()
    
    def createWidgets(self):
        #! outdated
        #menubar
        self.menubar.add_command(label='quit',command=self.quit)
        #control
        self.control.sections = []
        
        self.control.sections.append(tk.Button(self.control,text=self.child.name,bg=config.MCbutBgCol,command=self.butLab))
        self.control.sections[-1].grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        
        self.control.sections.append(tk.Button(self.control,text='Pattern-Laboratory',bg='white',command=self.butLab))
        self.control.sections[-1].grid(row=0, column=0, sticky='nsew', padx=2, pady=2)
        self.control.sections.append(tk.Button(self.control,text='Pattern-Viewer',bg='white',command=self.cmdViewer))
        self.control.sections[-1].grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
        #details
        #self.details.state = None
        self.details.content = {}
    
    def cmdChangeMode(self,mode):
        self.mode = mode
        self.child[self.mode].ShowDetails()
    
    def butLab(self):
        if self.lab == None or self.lab.winfo_exists() == 0:
            self.lab = tk.Toplevel()
            self.lab.resizable(width=False,height=False)
            self.lab.wm_title('RM-GoL Laboratory')
            self.lab.parent = self
            self.lab.active = 0
            self.lab.Bdimension = [config.LBwidth,config.LBheight]
            self.lab.Bborder = Utils.Border(width=config.LBwidth,height=config.LBheight)
            lab.createWidgets(self.lab)
            lab.cellClicked(self.lab,int(config.LBwidth/2),int(config.LBheight/2))
            lab.updateGrid(self.lab)
        if self.details.state != 'lab':
            self.details.state = 'lab'
            lab.createDetails(self)
        
