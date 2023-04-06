from turtle import Turtle
import math


class Ball(Turtle):

    def __init__(self, paddle, bricks):
        super().__init__()
        self.paddle = paddle
        self.bricks = bricks
        self.ycomp_v = -5  # motion component y
        self.xcomp_v = -5  # motion component x
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
        self.f_xpos = self.xcomp_v + self.f_xpos
        self.f_ypos = self.ycomp_v + self.f_ypos

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
            self.ycomp_v = -5  # velocity component x
            self.xcomp_v = -5  # velocity component y
            self.f_xpos = 0.0  # floating point xpos
            self.f_ypos = 0.0  # floating point ypos

        # detect paddle hit
        if self.f_ypos == -280 + 10 and (self.paddle.xpos - 50 <= self.f_xpos <= self.paddle.xpos + 50):
            if self.f_xpos <= self.paddle.xpos - 25:
                if self.xcomp_v >= -15:
                    self.xcomp_v += -5
            if self.f_xpos >= self.paddle.xpos + 25:
                if self.xcomp_v <= 15:
                    self.xcomp_v += 5
            self.ycomp_v *= -1

        # -- collision with brick --
        # check when ball crosses grid line (vertical or horizontal) into new grid cell
        # check if grid cell has visible turtle
        # if turtle is visible, make invisible and set ball position to edge and reverse velocity
        # otherwise ball continues moving in same direction

        next_x = self.xcomp_v + self.f_xpos
        next_y = self.ycomp_v + self.f_ypos

        # direction oriented based check
        bottom_limit = self.bricks.y_grid[0]

        # moving upwards
        if self.ycomp_v > 0 and self.f_ypos >= bottom_limit:
            for y_line in self.bricks.y_grid:
                if self.f_ypos <= y_line <= next_y:  # line cross detected
                    # check if turtle visible
                    brick = self.bricks.brick_at_xy(next_x, next_y)
                    if brick is not None and brick.isvisible():
                        brick.hideturtle()
                        self.f_ypos = y_line
                        self.ycomp_v *= -1
                        return
        # moving down
        if self.ycomp_v < 0 and self.f_ypos >= bottom_limit:
            for y_line in self.bricks.y_grid:
                if self.f_ypos >= y_line >= next_y:  # line cross detected
                    # check if turtle visible
                    brick = self.bricks.brick_at_xy(next_x, next_y)
                    if brick is not None and brick.isvisible():
                        brick.hideturtle()
                        self.f_ypos = y_line
                        self.ycomp_v *= -1
                        return

        # moving right
        if self.xcomp_v > 0 and self.f_ypos >= bottom_limit:
            for x_line in self.bricks.x_grid:
                if self.f_xpos <= x_line <= next_x:  # line cross detected
                    # check if turtle visible
                    brick = self.bricks.brick_at_xy(next_x, next_y)
                    if brick is not None and brick.isvisible():
                        brick.hideturtle()
                        # self.f_xpos = x_line
                        self.xcomp_v *= -1
                        return

        # moving left
        if self.xcomp_v < 0 and self.f_ypos >= bottom_limit:
            for x_line in self.bricks.x_grid:
                if next_x <= x_line <= self.f_xpos:  # line cross detected
                    # check if turtle visible
                    brick = self.bricks.brick_at_xy(next_x, next_y)
                    if brick is not None and brick.isvisible():
                        brick.hideturtle()
                        # self.f_xpos = x_line
                        self.xcomp_v *= -1
                        return
