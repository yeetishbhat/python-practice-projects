import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("us states game")
img = "blank_states_img.gif"
screen.addshape(img)

turtle.shape(img)
game_on = True
score = 0

df = pd.read_csv("50_states.csv")
states = df.state.to_list()

while game_on:

    answer = screen.textinput(title=f"guess the state {score}/50 ", prompt="write the name of the state").title()
    if answer in states:
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer]
        x = state_data.x.item()
        y = state_data.y.item()
        turtle.goto(x, y)
        t.write(f"{state_data.state.item()}")




screen.exitonclick()


