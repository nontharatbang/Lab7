from turtle import *

class Pole(object):
    def __init__(self, name = "", xpos = 0, ypos = 0, thick = 10, length = 100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

        self.t = Turtle()
        self.t.fillcolor("green")

    def showpole(self):
        self.t.pu()
        self.t.setposition(self.pxpos, self.pypos)
        self.t.pd()
        self.t.begin_fill
        
        for i in range(2):
            self.t.forward(self.pthick/2)
            self.t.left(90)
            self.t.forward(self.plength)
            self.t.left(90)
            self.t.forward(self.pthick/2)
        
        self.t.end_fill
        #self.t.pu()