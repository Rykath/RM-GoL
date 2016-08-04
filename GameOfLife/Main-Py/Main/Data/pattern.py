'''
Created on Aug 3, 2016

@author: Rykath
Package: Main.Data

Usage: class for single patterns
'''

import Main.utilities as Utils

class Pattern():
    type = "simple-pattern"
    scope = "internal"
    
    def __init__(self,ID):
        self.id = ID
        self.name = None
        self.mapL = None    # dead,living | 0,1
    
    def input(self,name=None,array=[[]]):
        if name != None:
            self.name = name
        if array != [[]]:
            self.mapL = Utils.Map(dimension=2,size=[len(array[0]),len(array)],default=0,valid=[0,1])
            for y in range(len(array)):
                for x in range(len(array[0])):
                    if array[y][x] == 1:
                        self.mapL.set([x,y],1)
        