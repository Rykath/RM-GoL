'''
Created on Apr 5, 2016

@author: Rykath
Package: Main.Data

Usage: Internal data-storage , classes
'''

import Main.Engine.base as Engine
import Main.Engine.compute as Compute
#from operator import pos

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
        self.heightA = []   #absolute height
        self.widthA  = []   #absolute width
        self.heightT = 0    #total height
        self.widthT = 0     #total width
        self.offsetX = []   #offset/speed for origin in x-direction, [left,right], absolute
        self.offsetY = []   #offset/speed for origin in y-direction, [up,down], absolute
        self.speed = [0,0]  #speed [x,y] for spaceships, sum of offsets, left&up is positive
        self.data = []      #contains data, 2-dimensional-array
        self.dataNum = []   #number of live cells
        self.count = []     #contains surrounding count, 2-dimensional-array, bounding box
        self.countNum = []  #cells in bounding box
    
    def mirror(self,X,Y):
        #X, Y = True/False
        if X:
            for i in range(self.period):
                for y in range(self.heightA[i]):
                    self.data[i][y].reverse()
                    self.count[i][y].reverse()
                    self.offsetX[i].reverse()
            self.speed[0] *= -1
        if Y:
            for i in range(self.period):
                self.data[i].reverse()
                self.count[i].reverse()
                self.offsetY[i].reverse()
            self.speed[1] *= -1
    
    def rotate(self):
        #actually doesn't rotate but mirrors around diagonal-axis
        for i in range(self.period):
            data = []
            count = []
            for x in range(self.widthA[i]):
                data.append([])
                count.append([])
                for y in range(self.heightA[i]):
                    data[x].append(self.data[i][y][x])
                    count[x].append(self.count[i][y][x])
            self.data[i] = data
            self.count[i] = count
        self.speed.reverse()
        self.offsetX, self.offsetY = self.offsetY, self.offsetX                    
    
    def compute(self,data,count):
        data,count = Engine.Resize(data,count)
        data,count,shift = Engine.Tick(data,count)
        x = True
        y = 0
        while x:
            if y != 0:
                data,count,shift = Engine.Tick(self.data[-1],self.count[-1])
            if data in self.data:
                pos = self.data.index(data)
                for i in range(1,len(self.data)-pos):
                    shift[0] += self.offsetX[i+pos][0]
                    shift[1] += self.offsetX[i+pos][1]
                    shift[2] += self.offsetY[i+pos][0]
                    shift[3] += self.offsetY[i+pos][1]
                if pos == len(self.data)-1 and shift == [0,0,0,0]:
                    self.type = 'Still-Life'
                elif shift == [0,0,0,0]:
                    self.type = 'Oscillator'
                else:
                    self.type = 'Spaceship'
                self.period = len(self.data)-pos
                del self.data[:pos]
                del self.dataNum[:pos]
                del self.count[:pos]
                del self.countNum[:pos]
                del self.heightA[:pos]
                del self.widthA[:pos]
                self.heightT = max(self.heightA)
                self.widthT = max(self.widthA)
                del self.offsetX[:pos]
                del self.offsetY[:pos]
                self.speed = [shift[0]-shift[1],shift[2]-shift[3]]
                x = False
            else:
                self.data.append(data)
                self.count.append(count)
                self.dataNum.append(Compute.dataNum(data))
                self.countNum.append(Compute.countNum(count))
                self.offsetX.append(shift[:2])
                self.offsetY.append(shift[2:])
                self.heightA.append(len(data))
                self.widthA.append(len(data[0]))
                y += 1
            if y == 500 or data == []:
                self.type = 'Error'
                x = False
