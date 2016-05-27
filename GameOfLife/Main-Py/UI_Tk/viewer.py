'''
Created on May 27, 2016

@author: Rykath
Package: UI_Tk

Usage: view patterns in database
'''

import Tkinter as tk

import UI_Tk.config as config

class GUIViewer():
    key = 'viewer'
    name = 'Pattern-Viewer'
    posControl = 0 #row-position in control-section
    
    def __init__(self, core, parent):
        self.core = core
        self.parent = parent
        self.wrtDetails = False #whether details were created already or not
    
    def ShowDetails(self,destroy=False):
        # destroy=True : other elements in details deleted instead of hidden
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
            self.parent.details.content[self.key].append(tk.Label(self.parent.details,text='Test',bg=config.MDlblCol))
            self.parent.details.content[self.key][-1].grid(row=0,column=0,sticky='nsew',padx=1,pady=1)
            self.wrtDetails = True
        
        