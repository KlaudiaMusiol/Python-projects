from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("purple")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SSSSCORE: {self.score}", align="center", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nScore: {self.score}", align="center", font=("Courier", 50, "normal"))