from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = -10
        self.y_move = -10
        # self.x_move *= -1
        # self.y_move *= -1


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_roof(self):
        self.y_move *= -1

    
    def bounce_wall(self):
        self.x_move *= -1

    
    def paddle_bounce(self, left_dir, xcor_paddle):
        self.sety = 230

        if (self.xcor() < xcor_paddle) and left_dir == False:
            self.y_move *= -1
            self.x_move *= -1
        
        elif (self.xcor() > xcor_paddle) and left_dir == False:
            self.y_move *= -1
        
        elif (self.xcor() > xcor_paddle) and left_dir == True:
            self.y_move *= -1
            self.x_move *= -1

        elif (self.xcor() < xcor_paddle) and left_dir == True:
            self.y_move *= -1
            


        # self.x_move *= -1