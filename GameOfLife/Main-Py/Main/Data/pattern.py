'''
Created on Aug 3, 2016

@author: Rykath
Package: Main.Data

Usage: class for single patterns
'''

import Utilities.map
import Main.settings
import Main.Engine.basic

class Pattern():
    type = "simple-pattern"
    scope = "internal"
    
    def __init__(self,ID):
        self.id = ID
        self.name = None
        self.computeLvl = 0
        self.type = None
        self.size = 0
        
        # layers
        self.mapL = Utilities.map.Layers()    # dead,living | 0,1
        self.mapC = Utilities.map.Layers()    # cell count  | 0-8
        self.rep = None     # point of repetition | end of pattern = state no REP
    
    def input(self,name=None,array=None):
        if name != None:
            self.name = name
        if array != None:
            self.mapL.addLayer(Utilities.map.Map2D(array=array,default=Main.settings.MapLdef,valid=Main.settings.MapLval).shrink(False)[1])
    
    def compute(self):
        iteration = 0
        done = False
        while not done and iteration < Main.settings.CmptMaxIter:
            # add next generation
            o = Main.Engine.basic.getNxtGen(self.mapL.getLayer(-1,False).expand(four=1,mutate=False)).shrink(False)
            d = [1-i for i in o[0][0]]
            for i in range(self.mapL.size):
                if o[1].array == self.mapL.getLayer(i).array:
                    self.rep = i
            if self.rep == None:
                self.mapL.addLayer(o[1],off=d)
            iteration += 1
        self.size = self.mapL.size
        self.mapC = Utilities.map.Layers()
        for i in range(self.size):
            o = Main.Engine.basic.getCount(self.mapL.getLayer(i,False).expand(four=1,mutate=False)).shrink(False)
            d = [1-i for i in o[0][0]]
            self.mapC.addLayer(o[1],off=d)
        self.computeLvl = 1
        if self.rep == 0 and self.size == 1:
            self.type = "stilllife"
        if self.rep != 0 and self.size-self.rep == 1:
            self.type = "stilllife-constructor"
        self.computeLvl = 2
    
    def export(self,short=True):
        e = ""
        if not short:
            e = "\n"
        s = "#simple-pattern#"+e
        s += "id:"+self.id+"|"+e
        if self.name != None:
            s += "name:"+self.name+"|"+e
        if self.computeLvl >= 2:
            s += "type:"+self.type+"|"+e
        if self.computeLvl >= 1:
            for I in range(2):
                s += ["mapl:","mapc:"][I]
                o = [self.mapL,self.mapC][I]
                for i in range(self.size):
                    if i != 0:
                        s += "."
                    for ii in range(2):
                        s += str(o.getLayer(i).size[ii])+"."+str(o.pos[i][ii])+"."
                    S = ""
                    for x in range(o.getLayer(i).size[0]):
                        for y in range(o.getLayer(i).size[1]):
                            S += str(o.getLayer(i).get([x,y]))
                    s += hex(int(S,[2,9][I]))[2:]
                s += "|"+e
        s += "end#"
        return s

'''
class Pattern_old():
    type = "simple-pattern"
    scope = "internal"
    
    def __init__(self,ID):
        self.id = ID
        self.name = None
        self.computeLvl = 0
        
        self.mapL = None    # dead,living | 0,1
        self.mapC = None    # cell count  | 0-8
    
    def input(self,name=None,array=[[]]):
        if name != None:
            self.name = name
        if array != [[]]:
            self.mapL = Utils.Map(dimension=3,size=[1,len(array[0]),len(array)],default=0,valid=[0,1])
            for y in range(len(array)):
                for x in range(len(array[0])):
                    if array[y][x] == 1:
                        self.mapL.set([x,y],1)
    
    def compute(self):
        if self.computeLvl == 0 and self.mapL != None:
            pass    # compute pattern-type and next generations
        if self.mapL != None:
            self.mapC = Utils.Map(dimension=self.mapL.dimension,size=self.mapL.size,default=0,valid=list(range(9)))
            # assuming dimension = 3 (t,x,y)
            for p in range(len(self.mapC.size[0])):
                for x in range(len(self.mapC.size[1])):
                    for y in range(len(self.mapC.size[2])):
                        v = 0
                        for X in range(-1,2):
                            for Y in range(-1,2):
                                a = self.mapL.get([p,x+X,y+Y])
                                if a != None and (X,Y) != (0,0):
                                    v += a
                        self.mapC.set([p,x,y],v)
'''
