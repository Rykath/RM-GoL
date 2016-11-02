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
    def __init__(self,size=None,default=None,valid=None,array=None):
        #-- size is list with 2 positive-integer entries
        #-- default can be anything
        #-- valid is list with anything as contents, if valid is empty all values are valid
        #-- array is 2-dimensional, rectangular list with only valid or default entries
        if size == None:
            size = [2,2]
        if array == None:
            array = []
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
        #-- pos is list with 2 integer entries
        for i in range(self.dimension):
            if pos[i] >= self.size[i] or pos[i] < self.size[i]*-1:
                return None
        return self.array[pos[0]][pos[1]]
    
    def set(self,pos,value):
        # set content at given position to given value
        #-- pos is list with 2 integer entries
        for i in range(self.dimension):
            if pos[i] >= self.size[i] or pos[i] < self.size[i]*-1:
                return None
        if  self.valid == None or value in self.valid:
            self.array[pos[0]][pos[1]] = value
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
        # returns difference or difference and shrinked map if mutate is False
        #get empty slices (False = empty, True = not empty)
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
        dist = [[0,0],[0,0]]
        if True in U:   #'True in V' has to be True as well
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
            return [dist]
        else:
            out = Map2D(size=size,default=self.default,valid=self.valid,array=array)
            return [dist,out]
    
    def expand(self,dist=[[0,0],[0,0]],four=0,mutate=True):
        # add default slices (rows/columns) at each side to expand array
        #-- dist is a list with 2 lists which contain 2 (positive) integers each
        #-- four is a (positive) integer
        if four != 0:
            dist=[[four,four],[four,four]]
        size = [self.size[0]+dist[0][0]+dist[0][1],self.size[1]+dist[1][0]+dist[1][1]]
        array = []
        for u in range(size[0]):
            array.append([])
            for v in range(size[1]):
                if u >= dist[0][0] and u < self.size[0]+dist[0][0] and v >= dist[1][0] and v < self.size[1]+dist[1][0]:
                    array[u].append(self.get([u-dist[0][0],v-dist[1][0]]))
                else:
                    array[u].append(self.default)
        if mutate:
            self.array = array
            self.size = size
        else:
            out = self.copy()
            out.array = array
            out.size = size
            return out
    
    def expandTo(self,size,mutate=True):
        # expands array to a given size if possible
        # shrinks the array otherwise to smallest possible
        #-- returns dist
        if mutate:
            obj = self
        else:
            obj = self.copy()
        dist = obj.shrink(True)[0]
        exp = [[0,0],[0,0]]
        for i in range(2):
            if obj.size[i] < size[i]:
                exp[i][0] = round((size[i]-obj.size[i])/2-0.25)
                exp[i][1] = round((size[i]-obj.size[i])/2+0.25)
        for i in range(2):
            for ii in range(2):
                dist[i][ii] = exp[i][ii]-dist[i][ii]
        obj.expand(dist=exp)
        if mutate:
            return [dist]
        else:
            return [dist,obj]

class Layers():
    '''
    contains multiple layers (2D-maps) with different sizes
    '''
    
    def __init__(self):
        self.data = []
        self.pos = []   # global offset
        self.size = 0
    
    def addLayer(self,layer,pos=None,off=None):
        # add a new layer
        #-- layer is Map2D
        #-- pos is [x,y] | global (rel to first) offset | dominant argument
        #-- off is [x,y] | relative to last offset
        if pos != None:
            p = pos.copy()
        elif off != None:
            if self.size != 0:
                p = [self.pos[-1][i]+off[i] for i in range(2)]
            else:
                p = off.copy()
        elif self.size != 0:
            p = self.pos[-1].copy()
        else:
            p = [0,0]
        self.data.append(layer.copy())
        self.pos.append(p)
        self.size += 1
    
    def get(self,pos):
        #-- pos is [i,x,y]
        if pos[0] >= self.size or pos[0] < self.size*-1:
            return None
        return(self.data[pos[0]].get(pos[1:]))
    
    def getLayer(self,pos,mutate=True):
        #-- pos is integer | index
        if pos >= self.size or pos < self.size*-1:
            return None
        if mutate:
            return(self.data[pos])
        else:
            return(self.data[pos].copy())