'''
Created on May 26, 2016

@author: Rykath
Package: Main

Usage: Utility-Classes & Functions
'''

def output(typ,message):
    if typ == "error":
        print("Error: "+message)
    elif typ == "console":
        print(message)

class Border():
    
    def __init__(self,left=None,right=None,up=None,down=None,array=None,array2=None,four=None,width=None,height=None,dimension=None):
        self.array = [0,0,0,0] # [left,right,up,down]
        if dimension != None and len(dimension) == 2:
            if width == None:
                width = dimension[0]
            if height == None:
                height = dimension[1]
        if width != None:
            self.array[0] = int(width/2)
            self.array[1] = int(width/2+width%2)
        if height != None:
            self.array[2] = int(height/2)
            self.array[3] = int(height/2+height%2)
        if four != None:
            self.array = [four,four,four,four]
        if array2 != None and len(array2) == 2:
            self.array = [array2[0],array2[0],array2[1],array2[1]]
        if array != None and len(array) == 4:
            self.array = array[:]
        if left != None:
            self.array[0] = left
            if right == None and width != None:
                self.array[1] = width-left
        if right != None:
            self.array[1] = right
            if left == None and width != None:
                self.array[0] = width-right
        if up != None:
            self.array[2] = up
            if down == None and height != None:
                self.array[3] = height-up
        if down != None:
            self.array[3] = down
            if up == None and height != None:
                self.array[2] = height-down
        self.update()
    
    def update(self):
        self.left = self.array[0]
        self.right = self.array[1]
        self.up = self.array[2]
        self.down = self.array[3]
        self.dict = {'left': self.array[0],'right': self.array[1],'up': self.array[2],'down': self.array[3]}
        if self.left == self.right: #horizontal
            self.x = self.left
        else:
            self.x = None
        if self.up == self.down: #vertical
            self.y = self.up
        else:
            self.y = None
        if self.x == self.y:
            self.all = self.x
        else:
            self.all = None
        self.array2 = [self.x,self.y]
        self.dict2 = {'x': self.x,'y': self.y}
        self.width = self.left + self.right
        self.height = self.up + self.down
        self.dimension = [self.width,self.height]
    
    def add(self,array=None,dimension=None,invert=False):
        if invert:
            if array != None:
                for i in range(len(array)):
                    array[i] *= -1
            if dimension != None:
                for i in range(len(dimension)):
                    dimension[i] *= -1
        if array != None and len(array) == 4:
            for i in range(4):
                self.array[i] += array[i]
        elif dimension != None and len(dimension) == 2:
            for i in range(2):
                self.array[2*i] += int(dimension[i]/2)
                self.array[2*i+1] += int(dimension[i]/2)
                if self.array[2*i+1]<self.array[2*i]:
                    self.array[2*i+1] += int(dimension[i]%2)
                else:
                    self.array[2*i] += int(dimension[i]%2)
        self.update()
        return self

class Map():
    
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
