# This class initializes the user's paddle
from turtle import Turtle


# size = left/right, color: color of the paddle for user selection
class CreatePaddle:
    def __init__(self, side, color):
        self.paddle = Turtle()
        self.initial_paddle(side, color)

    def initial_paddle(self, side, color):
        self.paddle.shape("square")
        self.paddle.speed("fastest")
        self.paddle.goto(side)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.color(color)

    # control user paddle, by going up/down
    def go_up(self):
        if self.paddle.ycor() <= 325:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 30)

    def go_down(self):
        if self.paddle.ycor() >= -320:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 30)
