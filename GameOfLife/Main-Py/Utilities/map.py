'''
Created on Aug 24, 2016

@author: Rykath
Package: Utilities

Usage: Classes concerning multi-dimensional lists or maps
'''

class Map():
    '''
    multi-dimensional list
    
    WORK IN PROGRESS (see Map2D)
    '''
    def __init__(self,dimension=2,size=[2,2],default=0,valid=[0,1]):
        self.dimension = dimension
        self.size = size
        self.valid = valid
        self.default = default
        self.array = []
        # build array
        self.expand(size)
    
    def get(self,pos):
        e = self.array
        try:
            for i in range(len(pos)):
                p = pos[i] #% self.size[i]
                e = e[p]
            return e
        except IndexError:
            return None
    
    def set(self,pos,value):
        e = self.array
        if not value in self.valid:
            value = self.default
        for i in range(len(pos)):
            p = pos[i] % self.size[i]
            if i == len(pos)-1:
                e[p] = value
            else:
                e = e[p]
    
    def expand(self,size):
        pos = []
        for d in range(self.dimension):
            pos.append(0)
            for i in range(len(pos)):
                pos[i] = 0
            r = True
            while r:
                # append one element at specific position
                a = self.array
                for i in range(d+1):
                    p = pos[i]
                    if i == self.dimension-1:
                        a.append(self.default)
                    elif i == d:
                        a.append([])
                    else:
                        a = a[p]
                # calculate new position (like nested for-loop)
                while self.get(pos) != None:
                    i = 0
                    pos[i] += 1
                    while pos[i] == size[i] and not i == d:
                        pos[i] = 0
                        i += 1
                        pos[i] += 1
                if pos[i] == size[i] and i == d:
                    r = False

class Map2D():
    '''
    special case of Map-class
    2-dimensional, rectangular
    '''
    dimension = 2
    def __init__(self,size=[2,2],default=0,valid=[0,1],array=[]):
        # assuming valid input
        #-- size is list with 2 positive-integer entries
        #-- default can be anything
        #-- valid is list with anything as contents, if valid is empty all values are valid
        #-- array is 2-dimensional, rectangular list with only valid or default entries
        self.size = size
        self.valid = valid
        self.default = default
        self.array = array
        # recompute size
        if self.array != []:
            self.size = [len(self.array),len(self.array[0])]
        # build array
        else:
            for u in range(self.size[0]):
                self.array.append([])
                for _ in range(self.size[1]):
                    self.array[u].append(self.default)
    
    def get(self,pos):
        # return content at given position
        # assuming valid input
        #-- pos is list with 2 integer entries
        for i in range(self.dimension):
            if pos[i] >= self.size[i] or pos[i] < self.size[i]*-1:
                return None
        return self.array[pos[0]][pos[1]]
    
    def set(self,pos,value):
        # set content at given position to given value
        # assuming valid input
        #-- pos is list with 2 integer entries
        for i in range(self.dimension):
            if pos[i] >= self.size[i] or pos[i] < self.size[i]*-1:
                return None
        if value in self.valid or self.valid == []:
            self.array[pos[0],pos[1]] = value
            return True
        return None
    
    def copy(self):
        # return copy of self
        out = Map2D()
        out.size = self.size[:]
        out.default = self.default
        out.valid = self.valid
        out.array = []
        for u in range(self.size[0]):
            out.array.append([])
            for v in range(self.size[1]):
                out.array[u].append(self.get([u,v]))
        return out
    
    def shrink(self,mutate=True):
        # delete default slices (rows/columns) at each side to shrink array
        # returns difference (as border)
        # get empty slices (False = empty, True = not empty)
        U = []
        V = []
        for u in range(self.size[0]):
            U.append(False)
            for v in range(self.size[1]):
                if len(V) <= v:
                    V.append(False)
                if self.get([u,v]) != self.default:
                    U[u] = True
                    V[v] = True
        if True in U:   # 'True in V' has to be True as well
            dist = [[0,0],[0,0]]
            for u in range(self.size[0]):
                if u == dist[0][0] and not U[u]:
                    dist[0][0] = u+1
            for u in range(self.size[0]-1,-1,-1):
                if u == self.size[0]-dist[0][1]-1 and not U[u]:
                    dist[0][1] = self.size[0]-u
            for v in range(self.size[1]):
                if v == dist[1][0] and not V[v]:
                    dist[1][0] = v+1
            for v in range(self.size[1]-1,-1,-1):
                if v == self.size[1]-dist[1][1]-1 and not V[v]:
                    dist[1][1] = self.size[1]-v
            array = []
            for u in range(dist[0][0],self.size[0]-dist[0][1]):
                array.append([])
                for v in range(dist[1][0],self.size[0]-dist[1][1]):
                    array[u-dist[0][0]].append(self.get([u,v]))
            size = [self.size[0]-dist[0][0]-dist[0][1],self.size[1]-dist[1][0]-dist[1][1]]
        else:
            array = []
            size = [0,0]
        if mutate:
            self.array = array
            self.size = size
        else:
            out = self.copy()
            out.array = array
            out.size = size
            return out

class Layers():
    '''
    contains multiple layers (2D-maps) with different sizes
    '''
    
    def __init__(self):
        self.data = []
        self.size = 0
    
    def addLayer(self):
        pass