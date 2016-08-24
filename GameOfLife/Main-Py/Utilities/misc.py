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