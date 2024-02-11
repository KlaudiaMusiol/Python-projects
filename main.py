from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
franek = Turtle(shape="turtle")
colors = ("red", "orange", "coral", "pink", "purple", "violet", "deeppink")


def start_position(one_turtle, turtle_number):
    one_turtle.penup()
    one_turtle.goto(x=-230, y=-200 + turtle_number * 50)


is_race_on = False

turtles = []
for color in colors:
    color = Turtle(shape="turtle")
    turtles.append(color)

no_of_turtles = 0
for turtle in turtles:
    no_of_turtles += 1
    turtle.color(colors[no_of_turtles - 1])
    start_position(turtle, no_of_turtles)

user_bet = screen.textinput("RACE", "Which turtle will win the race? Please enter the color:").lower()

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
