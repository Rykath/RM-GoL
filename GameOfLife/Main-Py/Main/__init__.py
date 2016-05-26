'''
Created on Apr 2, 2016

@author: Rykath

Main file
'''

class Core():
    
    def __init__(self):
        #Database
        self.Ddb = [] #database
        #Laboratory
        self.Lcp = None #current pattern

if __name__ == '__main__':
    import Tkinter as tk
    
    import UI_Tk.__init__ as UI
    
    core = Core()
    
    Wcontrol = UI.GUI(core=core)
    Wcontrol.mainloop()