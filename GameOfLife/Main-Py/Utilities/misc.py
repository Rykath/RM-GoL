'''
Created on Aug 24, 2016

@author: Rykath
Package: Utilities

Usage: various functions and classes
'''

def output(typ,message):
    if typ == "error":
        print("Error: "+message)
    elif typ == "warning":
        print("Warning: "+message)
    elif typ in ["console","debug","test"]:
        print(message)

def intToBaseX(n,b):
    if n == 0:
        d = [0]
    else:
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        d =  digits[::-1]
    keys = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
    if b > len(keys):
        return d
    else:
        s = ''
        for i in d:
            s += keys[i]
        return s

def baseXToInt(n,b):
    keys = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
    I = 0
    for i in range(len(n)):
        I += keys.index(n[i])*b**(len(n)-(i+1))
    return I

def baseXToBaseY(n,bX,bY):
    return intToBaseX(baseXToInt(n,bX),bY)