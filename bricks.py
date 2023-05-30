from turtle import Turtle
from random import choice

colors = ['yellow', 
        'orange',
         'red', 
         'violet', 
         'magenta', 
         'purple', 
         'navy', 
         'blue', 
         'skyblue', 
         'cyan', 
         'turquoise', 
         'lightgreen',
         'green', 
         'white']


class Brick(Turtle):
    def __init__(self, position):
        
        super().__init__()
        self.shape("square")
        self.color(choice(colors))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
