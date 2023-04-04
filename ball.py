from turtle import Turtle
import math


class Ball(Turtle):

    def __init__(self, paddle, blocks=None):
        super().__init__()
        self.paddle = paddle
        self.velocity = 5
        self.ycomp_v = -1  # velocity component x
        self.xcomp_v = -1  # velocity component y
        self.f_xpos = 0.0  # floating point xpos
        self.f_ypos = 0.0  # floating point ypos
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

        self.goto(math.floor(self.f_xpos), math.floor(self.f_ypos))

    def move_ball(self):
        # calculate new pos on floating point positions and velocity
        self.f_xpos = self.xcomp_v * self.velocity + self.f_xpos
        self.f_ypos = self.ycomp_v * self.velocity + self.f_ypos

        self.goto(math.floor(self.f_xpos), math.floor(self.f_ypos))

    def detect_collision(self):
        # walls
        if math.fabs(self.f_xpos) >= 300 - 10:
            self.xcomp_v *= -1

        if self.f_ypos >= 300 - 10:
            self.ycomp_v *= -1

        # bottom of screen is death
        if self.f_ypos <= -300:
            # log death

            # reset ball
            self.ycomp_v = -1  # velocity component x
            self.xcomp_v = -1  # velocity component y
            self.f_xpos = 0.0  # floating point xpos
            self.f_ypos = 0.0  # floating point ypos

        # detect paddle hit
        if self.f_ypos == -280 + 10 and (self.paddle.xpos - 50 <= self.f_xpos <= self.paddle.xpos + 50):
            self.ycomp_v *= -1
