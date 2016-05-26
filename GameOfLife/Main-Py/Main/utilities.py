'''
Created on May 26, 2016

@author: Rykath
Package: Main

Usage: Utility-Classes
'''

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