'''
Created on Jul 3, 2016

@author: Rykath
Package: Main.Interface

Usage: database related class & function for the UI
'''

import Main.Interface.common as Common

class UI_patternviewer():
    key = 'db-pv'
    '''
    gui    | name of GUI-Package used
    GUI    | GUI-Package
    frame  | GUI-Package object / window-instance
    '''
    
    def __init__(self,gui,core):
        self.gui = gui
        self.core = core
        self.GUI = Common.importGui(self.gui).database
        self.GUIc = Common.importGui(self.gui).common
        
        self.frame = self.GUI.create(self.key)
        self.frame.parent = self
        Common.menubar(self)
    
    def update(self):
        self.GUI.update(self.frame)
        