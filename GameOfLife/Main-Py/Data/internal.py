'''
Created on Apr 5, 2016

@author: Rykath
Package: Data

Usage: Internal data-storage , classes
'''

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
        self.committer = author    #put into database by, REQUIRED
        self.description = ''   #purpose/usage
        self.trivia = ''        #history
        
        #gathered info , everything is packed into arrays with index of current period
        self.period = None  #integer
        self.lengthA = []   #absolute length
        self.widthA  = []   #absolute width
        self.offsetX = []   #offset/speed for origin in x-direction, right is +
        self.offsetY = []   #offset/speed for origin in y-direction, up is +
        self.data = []      #contains data, 2-dimensional-array
        self.count = []     #contains surrounding count, 2-dimensional-array, bounding box
