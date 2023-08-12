from turtle import Turtle

move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.new_segments = []
        self.create_snake()
        self.head = self.new_segments[0]

    def create_snake(self):
        starting_position = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_position:
           self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.color("Green")
        segment.shape("square")
        segment.penup()
        segment.setpos(position)
        self.new_segments.append(segment)

    def extend(self):
        self.add_segment(self.new_segments[-1].position())


    def move(self):
        for seg_num in range(len(self.new_segments) - 1, 0, -1):
            new_x = self.new_segments[seg_num - 1].xcor()
            new_y = self.new_segments[seg_num - 1].ycor()
            self.new_segments[seg_num].setpos(new_x, new_y)
        self.head.forward(move_distance)

    # snake controls

    def up(self):
        if self.head.heading() != DOWN:
            self.new_segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.new_segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.new_segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.new_segments[0].setheading(RIGHT)
