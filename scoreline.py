# this class Initial the score line
from turtle import Turtle

FONT = ("courier", 40, "normal")


# cords = location of the score-line color: color of the score-line for user selection
class ScoreLine(Turtle):
    def __init__(self, cords, color):
        super().__init__()
        self.score = -1
        self.right_score = -1
        self.init_scoreline(cords, color)
        self.add_score()

    def init_scoreline(self, cords, color):
        self.color(color)
        self.penup()
        self.ht()
        self.goto(cords)

    # add score in case of winning
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score:{self.score}", align="center", font=FONT)


