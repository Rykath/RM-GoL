'''
Created on Jun 22, 2016

@author: Rykath
Package: Main

Core-class and related functions
'''

class Core():
    
    def __init__(self):
        self.running = True
        #Database
        self.Ddb = [] #pattern-database (loaded patterns)
        #Laboratory
        self.Lcp = None #current pattern
        