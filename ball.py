# This class initializes and controls the game ball
from turtle import Turtle
from time import sleep


# Game ball initialize (Color / Size / Speed / Shape / starting cords)
class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed("fast")
        self.ball.shape("circle")
        self.ball.setheading(70)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.04

    # Keeping the ball move forward
    def move_forward(self):
        y_cord = self.ball.ycor() + self.y_move
        x_cord = self.ball.xcor() + self.x_move
        self.ball.goto(x_cord, y_cord)

    # Detection of the ball hitting the wall
    def wall_reflect(self):
        if self.ball.ycor() > 375 or self.ball.ycor() < -375:
            self.y_move *= -1

    # Detection of the ball hitting the paddle
    def pad_touch(self, pad):
        if (self.ball.distance(pad.paddle) < 50 and self.ball.xcor() > 535)\
                or (self.ball.distance(pad.paddle) < 50 and self.ball.xcor() < -535):
            self.x_move *= -1
            self.move_forward()
            self.move_speed *= 0.8

    # Detection the exit of the ball from the game
    def out_of_boundary(self):
        if self.ball.xcor() > 590:
            return "right"
        elif self.ball.xcor() < -590:
            return "left"

    # Start a new game after one of the players loses
    def restart_game(self):
        sleep(1.5)
        self.ball.goto(0, 0)
        self.move_speed = 0.04



