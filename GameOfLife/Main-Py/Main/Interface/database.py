'''
Created on Jul 3, 2016

@author: Rykath
Package: Main.Interface

Usage: database related class & function for the UI
'''

class UI_patternviewer():
    key = 'db-pv'
    
    def __init__(self,gui):
        self.gui = gui
    
    def create(self):
        if self.gui == 'tk':
            import UI_Tk.database as GUI
        self.frame = GUI.create(self.key)
    
    def update(self):
        if self.gui == 'tk':
            import UI_Tk.database as GUI
        GUI.update(self.frame)
        