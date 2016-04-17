'''
Created on Apr 5, 2016

@author: Rykath
Package: Data

Usage: Internal data-storage , classes
'''

import E_std.__init__ as Engine
import E_std.compute as Compute

class Pattern():
    '''
    General Pattern, toplevel-class
    
    2-dimensional-arrays:
    data in rows
    [0][0] is top-left
    [y][x+1] is right
    [y+1][x] is down
    
    origin point:
    top-left, [0][0]
    '''
    
    def __init__(self,ID,author):
        #general
        self.ID = ID            #internal ID , REQUIRED
        self.type = ''          #empty = undiscovered
        self.name = ''          #empty = unknown/unnamed
        self.num = 0            #id in type   
        self.author = ''        #discovered by, empty = not specified yet
        self.committer = author #put into database by, REQUIRED
        self.description = ''   #purpose/usage
        self.trivia = ''        #history
        
        #gathered info , everything is packed into arrays with index of current period
        self.period = None  #integer
        self.lengthA = []   #absolute length
        self.widthA  = []   #absolute width
        self.lengthT = 0    #total length
        self.widthT = 0     #total width
        self.offsetX = []   #offset/speed for origin in x-direction, [left,right]
        self.offsetY = []   #offset/speed for origin in y-direction, [up,down]
        self.data = []      #contains data, 2-dimensional-array
        self.dataNum = []   #number of live cells
        self.count = []     #contains surrounding count, 2-dimensional-array, bounding box
        self.countNum = []  #cells in bounding box
    
    def compute(self,data,count):
        data,count = Engine.Resize(data,count)
        self.data.append(data)
        self.count.append(count)
        self.dataNum = Compute.dataNum(self.data[-1])
        self.countNum = Compute.countNum(self.count[-1])
        ##find oscillator
        #still-life
        data,count,shift = Engine.Tick(self.data[0],self.count[0])
        if data == self.data[0] and shift == [0,0,0,0]:
            self.period = 0
            self.type = 'Still-Life'
