from turtle import Turtle

colors = ["pink", "red", "orange", "yellow", "green", "blue", "purple", "cyan"]

# grid 12x8
# each brick is 25x10 px

brick_width = 50
brick_height = 20
grid_upper = 260
grid_lower = 100


class Bricks:
    def __init__(self):
        self.brick_array = []
        self.x_grid = []
        self.y_grid = []
        self.__init_bricks()
        self.__init_gridlines()

    def __init_bricks(self):
        for i in range(8):
            for j in range(12):
                new_brick = Turtle()
                new_brick.color(colors[i])
                new_brick.speed("fastest")
                new_brick.shape("square")
                new_brick.penup()
                new_brick.shapesize(stretch_wid=.9, stretch_len=2.4)
                brick_x = j * brick_width + brick_width / 2 - 300
                brick_y = -i * brick_height + 250
                new_brick.goto(brick_x, brick_y)

                self.brick_array.append(new_brick)

    def __init_gridlines(self):

        self.x_grid = range(-300 + brick_width, 300, brick_width)
        self.y_grid = range(grid_lower, grid_upper, brick_height)

        pass

    def brick_at_xy(self, x, y):
        for brick in self.brick_array:
            brick_x = brick.xcor()
            brick_y = brick.ycor()
            if brick_x - (brick_width / 2) <= x <= brick_x + (brick_width / 2) and \
                    brick_y - (brick_height / 2) <= y <= brick_y + (brick_height / 2):
                return brick
        return None
