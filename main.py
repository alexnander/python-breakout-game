from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Breakout Game")

paddle = Paddle()
ball = Ball(paddle)

# follow mouse location
ws = screen.getcanvas()
ws.bind('<Motion>', paddle.update_pos)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1/120)
    ball.move_ball()
    paddle.update()
    ball.detect_collision()

