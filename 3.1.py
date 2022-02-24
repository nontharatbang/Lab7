from turtle import *

class Disk(object):
    def __init__(self, name = "", xpos = 0, ypos = 0, height = 20, width = 40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

        self.t = Turtle()
        self.t.speed(0)
        self.t.fillcolor("blue")

    def showdisk(self):
        self.t.pu()
        self.t.setposition(self.dxpos, self.dypos)
        self.t.pd()
        self.t.begin_fill()
        
        for i in range(2):
            self.t.forward(self.dwidth/2)
            self.t.left(90)
            self.t.forward(self.dheight)
            self.t.left(90)
            self.t.forward(self.dwidth/2)
        
        self.t.end_fill()
        self.t.pu()
        
    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
    def cleardisk(self):
        self.t.clear()