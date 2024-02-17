from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("plum")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def r_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def r_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def l_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def l_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
