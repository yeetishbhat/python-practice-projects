from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10


    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)

    def bounce(self):
        self.y *= -1

    def paddle_bounce(self):
        self.x *= -1

    def reset(self):
        self.goto(0,0)