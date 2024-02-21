import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from turtle_crossing_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("MistyRose")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.turtle_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.xcor() < -320:
            car_manager.all_cars.remove(car)

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > FINISH_LINE_Y:
        player.go_to_starting_position()
        car_manager.increase_speed()
        scoreboard.level_up()

screen.exitonclick()
