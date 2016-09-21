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
        self.menu.append(['button','Step',self.nxtGen])
        self.menu.append(['menu','Move',[['button',['Up','Down','Left','Right'][i],partial(self.move,[[0,-1],[0,1],[-1,0],[1,0]][i])]for i in range(4)]])
        self.GUIc.menubar(self.frame,self.menu)
        
        self.reset()
    
    def update(self):
        self.boardC = Engine.getCount(self.boardL)
        self.GUI.update(self.frame,self)
    
    def reset(self):
        self.boardSize = Settings.labSize[:]
        self.board = Utilities.map.Map2D(size=Settings.labSize)
        for x in range(self.board.size[0]):
            for y in range(self.board.size[1]):
                self.board.set([x,y],self.GUIc.make('button',self.frame,command=partial(self.boardClick,[x,y])))
        self.boardL = Utilities.map.Map2D(size=Settings.labSize,default=0,valid=[0,1])
        self.boardC = Engine.getCount(self.boardL)
        self.boardMove = [0,0]
    
    def boardClick(self,pos):
        self.boardL.set([self.boardMove[i]+pos[i] for i in range(2)],abs(self.boardL.get([self.boardMove[i]+pos[i] for i in range(2)])-1)) # invert the value
    
    def nxtGen(self):
        self.boardL = Engine.getNxtGen(self.boardL,self.boardC)
        self.update()
    
    def move(self,pos):
        self.boardMove = [self.boardMove[i]+pos[i] for i in range(2)]
        for i in range(2):
            if self.boardMove[i]+Settings.labSize[i] > self.boardSize[i]:
                dist = [[0,0],[0,0]]
                dist[i][1] = self.boardMove[i]+Settings.labSize[i]-self.boardSize[i]
                self.boardSize[i] = self.boardMove[i]+Settings.labSize[i]
                self.boardL.expand(dist=dist)
            elif self.boardMove[i] < 0:
                dist = [[0,0],[0,0]]
                dist[i][0] = 0-self.boardMove[i]
                self.boardSize[i] += 0-self.boardMove[i]
                self.boardL.expand(dist=dist)
                self.boardMove[i] = 0
        self.update()
