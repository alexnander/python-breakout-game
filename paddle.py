import turtle
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=.75, stretch_len=5)
        self.goto(0, -280)
        self.xpos = 0

    def update_pos(self, event):
        self.xpos = event.x - 300

    def update(self):
        self.goto(self.xpos, -280)
