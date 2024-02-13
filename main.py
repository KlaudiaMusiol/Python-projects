from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("deeppink")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_score()
        snake.extend_snake()
        food.refresh_food()

    if snake.segments[0].xcor() > 295 or snake.segments[0].ycor() < -295 or snake.segments[0].ycor() > 295 or \
            snake.segments[0].xcor() < -295:
        game_on = False
        scoreboard.game_over()

    slice_of_segments = snake.segments[1:]

    for segment in slice_of_segments:
        if snake.segments[0].distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
