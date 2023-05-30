from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick

import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BreakOut Game")
screen.tracer(0)

paddle = Paddle((-25, -260))
ball = Ball()


bricks_list = [(Brick((-355 + itemx * 70, 280 - itemy * 30))) for itemx in range(11) for itemy in range(9)]


screen.listen()

screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")


game_is_on = True

counter = 0.1

direction = 0
left_dir = False
x_t = 0

while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(counter)

    #### bounce roof
    if ball.ycor() > 300:
        ball.bounce_roof()

    ##### bounce walls

    if abs(ball.xcor()) > 380:
        ball.bounce_wall()

    ### direction for paddle hit
    if direction == 0:
        x_t = ball.xcor()       
        direction += 1 
        
    elif direction == 1:
        left_dir = x_t > ball.xcor()
        direction += 1
    else:
        direction = 0

    #### bounce with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -230:

        ball.paddle_bounce(left_dir, paddle.xcor())

    #### ball is out, fall down
    if ball.ycor() < -280:
        # ball.y_move *= -1
        ball.goto(-10, -10)
    
    ##### if ball hit a brick

    for item in bricks_list:
        if item.distance(ball) < 20:
            ball.y_move *= -1
            item.clear()
            item.goto(2000, 2000)


screen.exitonclick()
