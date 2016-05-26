'''
Created on May 26, 2016

@author: Rykath
Package: Main

Usage: Utility-Classes
'''

class Border():
    
    def __init__(self,left=None,right=None,up=None,down=None,border=None,four=None):
        self.array = [0,0,0,0] # [left,right,up,down]
        if four != None:
            self.array = [four,four,four,four]
        if border != None and len(border) == 4:
            self.array = border[:]
        if left != None:
            self.array[0] = left
        if right != None:
            self.array[1] = right
        if up != None:
            self.array[2] = up
        if down != None:
            self.array[3] = down
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
            