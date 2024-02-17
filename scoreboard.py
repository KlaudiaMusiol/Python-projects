from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("plum")
        self.penup()
        self.hideturtle()
        self.left_player_score = 0
        self.right_player_score = 0
        self.update_scoreboard()

    def point_left_player(self):
        self.left_player_score += 1
        self.update_scoreboard()

    def point_right_player(self):
        self.right_player_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-60, y=200)
        self.write(self.left_player_score, align="center", font=("Courier", 50, "italic"))
        self.goto(60, 200)
        self.write(self.right_player_score, align="center", font=("Courier", 50, "italic"))
