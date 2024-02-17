from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("violetred4")
screen.title("PongPong")

ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.r_paddle_up, "Up")
screen.onkey(r_paddle.r_paddle_down, "Down")
screen.onkey(l_paddle.l_paddle_up, "w")
screen.onkey(l_paddle.l_paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_top_bottom()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_from_paddle()

    if ball.xcor() > 380:
        ball.start_position()
        scoreboard.point_left_player()
        ball.ball_speed *= 0.1

    if ball.xcor() < -380:
        ball.start_position()
        scoreboard.point_right_player()
        ball.ball_speed *= 0.1


screen.exitonclick()
