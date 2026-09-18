# import turtle
#
# tim = turtle.Turtle()
# screen = turtle.Screen()
#
# def forward():
#     tim.forward(10)
# def back():
#     tim.backward(10)
# def left():
#     tim.left(10)
# def right():
#     tim.right(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.goto(0,0)
#     tim.setheading(0)
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=forward)
# screen.onkey(key="s", fun=back)
# screen.onkey(key="a", fun= left)
# screen.onkey(key="d", fun= right)
# screen.onkey(key="q", fun= clear)
#
#
#
# screen.exitonclick()


import turtle

tim = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "make your bet", prompt="enter the color of the turtle :")
print(user_bet)

for i in range(6):


screen.exitonclick()