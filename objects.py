import random
import vpython as vp

"""Molecule class"""
class Molecule:
    def __init__(self, size, pos):
        self.position = vp.vector(pos[0]+random.randrange(-2, 2),
                                  pos[1]+random.randrange(-2, 2),
                                  pos[2])
        self.size = size
        self.color = random.choice([vp.color.blue,vp.color.red])
    
    def create(self):
        self.instance = vp.sphere(pos=self.position,
                          radius=self.size, color=self.color, make_trail=False)
        return self.instance

"""Container class"""    
class Container:
    def __init__(self, height, width, thickness):
        self.height = height
        self.width = width
        self.thickness = thickness
        
    def create(self):
        border_up = vp.box(pos=vp.vector(0,self.height/2,0), 
                           length=self.width+self.thickness, height=self.thickness)
        border_down = vp.box(pos=vp.vector(0,-self.height/2,0), 
                             length=self.width+self.thickness, height=self.thickness)
        border_left = vp.box(pos=vp.vector(-self.width/2,0,0), 
                             length=self.thickness, height=self.height)
        border_right = vp.box(pos=vp.vector(self.width/2,0,0), 
                              length=self.thickness, height=self.height)
        return border_up, border_down, border_left, border_right
    
    