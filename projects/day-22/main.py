import turtle
import paddel
import ball
import time
import scoreboard



screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

paddle_1 = paddel.Paddel((350,0))
paddle_2 = paddel.Paddel((-350,0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()


screen.listen()
screen.onkey(paddle_1.move_up, "Up")
screen.onkey(paddle_1.move_down, "Down")

screen.onkey(paddle_2.move_up, "w")
screen.onkey(paddle_2.move_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    if paddle_1.distance(ball) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()

    if paddle_2.distance(ball) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 390 :
        ball.reset()
        scoreboard.l_score += 1
        scoreboard.update()
        ball.paddle_bounce()

    if ball.xcor() < -390:
        ball.reset()
        scoreboard.r_score += 1
        scoreboard.update()
        ball.paddle_bounce()



screen.exitonclick()

