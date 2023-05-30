from turtle import Turtle

STEP = 20

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    
    def go_left(self):
        if self.xcor() > -335:
            # print("Estoy en left", self.xcor())
            self.goto(self.xcor() - STEP ,self.ycor())

    def go_right(self):
        if self.xcor()  < 335:
            # print("Estoy en right",  self.xcor())
            self.goto(self.xcor() + STEP ,self.ycor())