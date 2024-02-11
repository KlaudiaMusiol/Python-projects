from turtle import Turtle, Screen

franek = Turtle()
screen = Screen()


def move_forward():
    franek.forward(10)


def move_backward():
    franek.backward(10)


def counter_clockwise():
    franek.left(10)


def clockwise():
    franek.right(10)


def clear_back():
    franek.clear()
    franek.up()
    franek.home()
    franek.down()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_back)

screen.exitonclick()
