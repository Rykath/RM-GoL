'''
Created on Sep 18, 2016

@author: Rykath
Package: Main.Interface

Usage: laboratory related class & function for the UI
'''

from functools import partial

import Main.Interface.common as Common
import Main.settings as Settings
import Utilities.map
import Main.Engine.basic as Engine

class UI_laboratory():
    key = 'lab'
    '''
    gui    | name of GUI-Package used
    GUI    | GUI-Package
    frame  | GUI-Package object / window-instance
    '''
    
    def __init__(self,gui,core):
        self.gui = gui
        self.core = core
        self.GUI = Common.importGui(self.gui).laboratory
        self.GUIc = Common.importGui(self.gui).common
        
        self.frame = self.GUIc.create(self.key)
        self.frame.parent = self
        
        Common.menubar(self)
        self.menu.append(['button','Reset',self.reset])
        #self.menu.append(['button','Step',self.nxtGen])
        
        self.reset()
    
    def update(self):
        self.boardC = Engine.getCount(self.boardL)
        self.GUI.update(self.frame,self.board,self.boardL,self.boardC)
    
    def reset(self):
        self.board = Utilities.map.Map2D(size=Settings.labSize)
        for x in range(self.board.size[0]):
            for y in range(self.board.size[1]):
                self.board.set([x,y],self.GUIc.make('button',self.frame,command=partial(self.boardClick,[x,y])))
        self.boardL = Utilities.map.Map2D(size=Settings.labSize,default=0,valid=[0,1])
        self.boardC = Engine.getCount(self.boardL)
    
    def boardClick(self,pos):
        self.boardL.set(pos,abs(self.boardL.get(pos)-1)) # invert the value