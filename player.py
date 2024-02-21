from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("ForestGreen")
        self.shape("turtle")
        self.penup()
        self.right(270)
        self.go_to_starting_position()

    def turtle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)
