'''
Created on Apr 6, 2016

@author: Rykath
Package: E_std

Usage: main file for Engine with standard-algorithm
'''

def calcCount(data):
    count = []
    for y in range(len(data)):
        count.append([])
        for x in range(len(data[y])):
            count.append(calcAround(data,x,y))
    return count

def calcAround(data,x,y):
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
        s += data[x+1][y-1]
    return s
        
            