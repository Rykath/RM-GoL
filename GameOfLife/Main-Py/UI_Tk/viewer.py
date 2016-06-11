'''
Created on May 27, 2016

@author: Rykath
Package: UI_Tk

Usage: view patterns in database
'''

import Tkinter as tk
from functools import partial

import UI_Tk.config as config

class GUIViewer():
    key = 'viewer'
    name = 'Pattern-Viewer'
    posControl = 0 #row-position in control-section
    
    def __init__(self, core, parent):
        self.core = core
        self.parent = parent
        self.wrtDetails = False #whether details were created already or not
        
        self.browserState = 0
        self.selected = None
    
    def ShowDetails(self,destroy=False):
        # destroy=True : other elements in details deleted instead of hidden
        if destroy:
            self.parent.details.content.clear()
            for i in self.parent.child:
                self.parent.child[i].wrtDetails = False
        for i in self.parent.details.content:
            for ii in self.parent.details.content[i]:
                ii.grid_remove()
        if not self.wrtDetails:
            self.parent.details.content[self.key] = []
            self.CreateWidgets(self.parent.details.content[self.key])
            self.wrtDetails = True
        self.ShowWidgets(self.parent.details.content[self.key])
    
    def CreateWidgets(self,content):
        content.append([tk.Label(self.parent.details,text='Pattern-Viewer',bg=config.MDlblCol),0,0,1,2])
        for i in range(config.VBheight):
            content.append([tk.Button(self.parent.details,bg=config.MDbutCol,command=partial(self.BrowserSelected,i)),i+1,0,1,1])
        content.append([tk.Button(self.parent.details,text='page up',bg=config.MDlblCol,command=partial(self.Browser,-1)),1,1,1,1])
    
    def ShowWidgets(self,content):
        for i in range(len(content)):
            content[i][0].grid(row=content[i][1],column=content[i][2],rowspan=content[i][3],columnspan=content[i][4],sticky='nsew',padx=1,pady=1)
    
    def Browser(self,scroll=0):
        if scroll != 0 and self.browserState + scroll >= 0 and self.browserState + scroll < len(self.core.Ddb)-config.VBheight:
            self.browserState += scroll
        for i in range(config.VBheight):
            if i+self.browserState < len(self.core.Ddb):
                self.parent.details.content[self.key][i+1][0].config(text=self.core.Ddb[i+self.browserState].ID+" | "+self.core.Ddb[i+self.browserState].name)
            else:
                self.parent.details.content[self.key][i+1][0].config(text='None')
    
    def BrowserSelected(self,index):
        self.selected = index + self.browserState
        