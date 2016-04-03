'''
Created on Apr 2, 2016

@author: Rykath

Main file
'''
import Tkinter as tk

import UI_Tk.__init__ as UI
#print "hello world"

window1 = tk.Tk()
UI.GUI(window1).pack(side="top", fill="both", expand=True)
#window1.master.title('RM-GoL')
window1.mainloop()