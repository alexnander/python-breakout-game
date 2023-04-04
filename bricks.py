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
                new_brick.shapesize(stretch_wid=1, stretch_len=2.50)
                brick_x = j * brick_width + brick_width / 2 - 300
                brick_y = -i * brick_height + brick_height / 2 + 250
                new_brick.goto(brick_x, brick_y)

                self.brick_array.append(new_brick)

    def __init_gridlines(self):
        # init x grid
        for i in range(12):
            self.x_grid.append(i*brick_width + 25 - 300)
        # init y grid
        for i in range(9):
            self.y_grid.append(i*brick_height + 100)

        pass
