import turtle
import time
import snake
import food
import scoreboard



screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:

        food.refresh()
        scoreboard.score += 1
        scoreboard.update()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        # food.game_over()
        # screen.update()
        scoreboard.reset()
        snake.reset()

    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            # food.game_over()
            # screen.update()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
