'''
Created on Aug 17, 2016

@author: Rykath
Package: Engine

Usage: Basic low-level functions for engine
'''

import Utilities.map

def generation(start):
    # computes next generation
    # start is 2D-array (rectangular)
    # size of grid is always increased
    out = []
    rules = [[3],[2,3]]  # set cell to live if right number of neighbours and state 0 or 1 respectively
    for x in range(len(start)+2):
        out.append([])
        for y in range(len(start[0])+2):
            if x in [0,len(start)+1] or y in [0,len(start[0])+1]:
                v = 0
            else:
                v = start[x-1][y-1]
            c = 0
            for X in range(-1,2):
                for Y in range(-1,2):
                    if (X,Y) != (0,0) and x+X > 0 and x+X < len(start)+1 and y+Y > 0 and y+Y < len(start[0])+1:
                        c += start[x+X-1][y+Y-1]
            if c in rules[v]:
                V = 1
            else:
                V = 0
            out[x].append(V)
    return out

# MAP-2D
def getCount(mapL):
    # returns Map2D with count of cells
    #-- mapL is Map2D
    #-- output has same size as input
    mapC = Utilities.map.Map2D(size=mapL.size,default=0,valid=range(9))
    for x in range(mapL.size[0]):
        for y in range(mapL.size[1]):
            c = 0
            for X in range(-1,2):
                for Y in range(-1,2):
                    if (X,Y) != (0,0) and x+X > 0 and x+X < mapC.size[0]+1 and y+Y > 0 and y+Y < mapC.size[1]+1:
                        c += mapL.get([x+X-1,y+Y-1])
            mapC.set([x,y],c)
    return mapC

def getNxtGen(mapL,mapC,rules=[[3],[2,3]]):
    # returns Map2D with cells of next generation
    #-- mapL & mapC are Map2D with same size
    #-- output is same size as input
    if mapC == None:
        mapC = getCount(mapL)
    mapLN = Utilities.map.Map2D(size=mapL.size,default=0,valid=[0,1])
    for x in range(mapL.size[0]):
        for y in range(mapL.size[1]):
            if mapC.get([x,y]) in rules[mapL.get([x,y])]:
                mapLN.set([x,y],1)
    return mapLN
    