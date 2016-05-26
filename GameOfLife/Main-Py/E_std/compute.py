'''
Created on Apr 17, 2016

@author: Rykath
Package: E_std

Usage: Functions for computing patterns, Laboratory/Data
'''

#COMPUTING
def dataNum(data):
    num = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            num += data[y][x]
    return num

def countNum(count):
    num = 0
    for y in range(len(count)):
        for x in range(len(count[y])):
            if count[y][x] > 0:
                num += 1
    return num

#COMMANDS
def rotate(pattern,direction):
    if direction == 'cw':
        pattern.rotate()
        pattern.mirror(True,False)
    elif direction == 'ccw':
        pattern.rotate()
        pattern.mirror(False,True)

def mirror(pattern,direction):
    if direction == 'x':
        pattern.mirror(True,False)
    elif direction == 'y':
        pattern.mirror(False,True)

def resize(frame,border):
    for i in border.array:
        if i < 0:
            i = 0
    frame.lab.Bborder = border.array[:]

def move(frame,border):
    for i in range(4):
        if frame.lab.Bborder[i] + border.array[i] >= 0:
            frame.lab.Bborder[i] += border.array[i]
        else:
            frame.lab.Bborder[i] = 0

        