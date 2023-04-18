from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake_body()
        self.head = self.segments[0]

    def create_snake_body(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # works like a GIF
        # start from the last segment, will take place of second last segment
        # second last will take place of 3rd last, so on..
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x, new_y = self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # move the 1st segment to desired position - move forward
        self.head.forward(MOVE_DISTANCE)

    # up - 90, down - 270, left - 180, right - 0
    # heading() -- 270 go to east - then go to desired   360-270=90 turtle.left(90) turtle.le
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # heading = self.segments[0].heading()
        # self.segments[0].left(360-heading+90) # go to east facing 0 deg

    def down(self):
        if self.head.heading() !=  UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

