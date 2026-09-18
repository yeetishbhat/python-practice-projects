import turtle


STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for seg in STARTING_POSITION:
            self.add_segment(seg)

    def add_segment(self,position):
        new_part = turtle.Turtle("square")
        new_part.penup()
        new_part.color("white")
        new_part.goto(position)
        self.snake_body.append(new_part)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add(self):
        new_part = turtle.Turtle("square")
        new_part.penup()
        new_part.color("white")
        self.snake_body.append(new_part)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]