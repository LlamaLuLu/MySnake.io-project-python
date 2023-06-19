from turtle import Turtle
MOVE_DISTANCE = 20  # constants
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # attribute to make code easier

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        # adds segment to snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for square in range(len(self.segments) - 1, 0, -1):  # last segment goes to 2nd last's position
            new_x = self.segments[square - 1].xcor()
            new_y = self.segments[square - 1].ycor()
            self.segments[square].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # can't change to opp direction while moving
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

