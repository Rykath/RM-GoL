'''
Created on Apr 6, 2016

@author: Rykath
Package: E_std

Usage: main file for Engine with standard-algorithm
'''

import math
import copy

def Tick(data,count=None,size=None):
    #returns data,count,shift
    data,count,v,u = Resize(data,count,True)
    shift = [] #left,right,top,bottom
    for i in range(len(v)):
        shift.append(v[i]-u[i])
    dataN = []
    for y in range(len(data)):
        dataN.append([])
        for x in range(len(data[y])):
            if ( data[y][x] == 1 and count[y][x] in [2,3] )or( data[y][x] == 0 and count[y][x] in [3]):
                dataN[y].append(1)
            else:
                dataN[y].append(0)
    dataN,count,v,u = Resize(dataN,None,True)
    for i in range(len(v)):
        shift[i] += v[i]-u[i]
    if size != None:
        dataN,count = Extendto(size,dataN,count)
    return (dataN,count,shift)

def Resize(data,count=None,retB=False):
    #returns resized data & count
    #generates count if None
    testY = []
    testX = 0
    freeY = []
    freeX = []
    border = [0,0,0,0] #left,right,top,bottom
    borderE = [0,0,0,0] #left,right,top,bottom
    #extend
    for y in [0,-1]:
        for x in range(len(data[y])):
            if data[y][x] == 1:
                borderE[2+abs(y)] = 1
    for x in [0,-1]:
        for y in range(len(data)):
            if data[y][x] == 1:
                borderE[abs(x)] = 1
    data = Extend(borderE,data)
    if 1 in borderE or count == None:
        count = Count(data)
    #shrink
    for y in range(len(count)):
        testX = 0
        for x in range(len(count[y])):
            if y == 0:
                testY.append(0)
            testX += count[y][x]
            testY[x] += count[y][x]
        if testX == 0:
            freeX.append(y)
    for i in range(len(testY)):
        if testY[i] == 0:
            freeY.append(i)
    for i in range(len(freeY)):
        if border[0] == freeY[i]:
            border[0] += 1
        if len(data[0])-border[1]-1 == freeY[-1*(i+1)]:
            border[1] += 1
    for i in range(len(freeX)):
        if border[2] == freeX[i]:
            border[2] += 1
        if len(data)-border[3]-1 == freeX[-1*(i+1)]:
            border[3] += 1
    dataN = []
    countN = []
    for y in range(len(data)-border[2]-border[3]):
        dataN.append([])
        countN.append([])
        for x in range(len(data[0])-border[0]-border[1]):
            dataN[y].append(data[y+border[2]][x+border[0]])
            countN[y].append(count[y+border[2]][x+border[0]])
    if retB == True:
        return (dataN,countN,borderE,border)
    else:
        return (dataN,countN)

def Extendto(size,data,count=None):
    #!! BUGGED
    #!! outdated (replaced by redrawGrid)
    #auto-center
    border = [0,0,0,0]
    if len(data[0]) < size[0]:
        border[0] = int(math.floor((size[0]-len(data[0]))/2))
        border[1] = int(math.floor((size[0]-len(data[0]))/2)+(size[0]-len(data[0]))%2)
    if len(data) < size[1]:
        border[2] = int(math.floor((size[1]-len(data))/2))
        border[3] = int(math.floor((size[1]-len(data))/2)+(size[1]-len(data))%2)
    return Extend(border,data,count)

def Extend(border,dataIn,countIn=None):
    #Extends data & count
    #border=[left,right,top,bottom] all positive (or zero)
    data = copy.deepcopy(dataIn)
    if countIn != None:
        count = copy.deepcopy(countIn)
    else:
        count = None
    if border[0] != 0:
        for y in range(len(data)):
            for _ in range(border[0]):
                data[y].insert(0,0)
                if count != None:
                    count[y].insert(0,0)
    if border[1] != 0:
        for y in range(len(data)):
            for _ in range(border[1]):
                data[y].append(0)
                if count != None:
                    count[y].append(0)
    if border[2] != 0:
        for _ in range(border[2]):
            data.insert(0,[])
            if count != None:
                count.insert(0,[])
            for _ in range(len(data[-1])):
                data[0].append(0)
                if count != None:
                    count[0].append(0)
    if border[3] != 0:
        for _ in range(border[3]):
            data.append([])
            if count != None:
                count.append([])
            for _ in range(len(data[0])):
                data[-1].append(0)
                if count != None:
                    count[-1].append(0)
    if count != None:
        return (data,count)
    else:
        return (data)

def Count(data):
    # returns array with cell-count for each cell
    count = []
    for y in range(len(data)):
        count.append([])
        for x in range(len(data[y])):
            count[y].append(CellCount(data,x,y))
    return count

def CellCount(data,x,y):
    # returns cell-count
    s = 0
    if x != 0:
        s += data[y][x-1]
    if y != 0:
        s += data[y-1][x]
    if x != 0 and y != 0:
        s += data[y-1][x-1]
    if x != len(data[0])-1:
        s += data[y][x+1]
    if y != len(data)-1:
        s += data[y+1][x]
    if x != len(data[0])-1 and y != len(data)-1:
        s += data[y+1][x+1]
    if x != len(data[0])-1 and y != 0:
        s += data[y-1][x+1]
    if x != 0 and y != len(data)-1:
        s += data[y+1][x-1]
    return s
        
            