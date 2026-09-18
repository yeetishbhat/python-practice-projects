import turtle
import random

timmy = turtle.Turtle()
#
# directions = [0,90,180,270]
# colors = ["red","blue","green","yellow","cyan"]
# timmy.shape("turtle")
# timmy.speed("fastest")
# turtle.colormode(255)
# angle = 0
#
# # for i in range(100):
# #     timmy.forward(50)
# #     timmy.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
# #     timmy.seth(random.choice(directions)
#
# for i in range(90):
#      timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#      timmy.setheading(angle)
#      angle += 4
#      timmy.circle(100)
#
# screen = turtle.Screen()
# screen.exitonclick()

# import colorgram
#
# color = colorgram.extract("test.jpg",25)
#
# print(color)
#
# color_rgb = []
#
# for item in color:
#      r= item.rgb.r
#      g= item.rgb.g
#      b= item.rgb.b
#      color_rgb.append((r,g,b))
#
# print(color_rgb)

color_list = [(199, 175, 117), (125, 36, 24), (169, 106, 56), (186, 158, 52), (206, 219, 210), (5, 57, 84), (222, 224, 227), (109, 67, 84), (41, 36, 35), (111, 161, 175), (20, 122, 175), (64, 153, 137), (88, 141, 55), (75, 39, 47), (9, 67, 47), (182, 97, 79), (133, 40, 43), (179, 201, 186), (206, 200, 148), (146, 173, 161), (169, 155, 159), (212, 183, 175), (35, 76, 60)]
turtle.colormode(255)
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()

x = -250
y = -250
for item in range(10):
     timmy.goto(x, y)
     for item in range(10):
       timmy.dot(20, random.choice(color_list))
       timmy.forward(50)
     y= y+50



screen = turtle.Screen()
screen.exitonclick()
