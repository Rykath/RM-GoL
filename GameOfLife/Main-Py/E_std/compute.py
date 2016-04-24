'''
Created on Apr 17, 2016

@author: Rykath
Package: E_std

Usage: Functions for computing patterns, Laboratory/Data
'''

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

        