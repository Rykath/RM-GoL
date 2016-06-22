'''
Created on Apr 2, 2016

@author: Rykath
Package: Main

Main file
'''

class Core():
    
    def __init__(self):
        #Database
        self.Ddb = [] #pattern-database (loaded patterns)
        #Laboratory
        self.Lcp = None #current pattern


if __name__ == '__main__':
    #import Tkinter as tk
    
    import UI_Tk.__init__ as UI
    import Main.Data.__init__ as Data
    
    core = Core()
    
    Wcontrol = UI.GUI(core=core)
    Wcontrol.mainloop()