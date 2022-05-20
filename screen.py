# This class is responsible for initializing the game screen
from turtle import Screen, Turtle

SCREENSIZE = 1200


# Initialize the screen settings (Color / size)
class MyScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        self.seperator = Turtle()
        self.screen.setup(width=SCREENSIZE, height=SCREENSIZE-400)
        self.make_seperator()
        self.screen.update()

    # Creating screen seperator in the middle of the screen
    def make_seperator(self):
        self.seperator.color("white")
        self.seperator.speed("fastest")
        self.seperator.hideturtle()
        self.seperator.pensize(5)
        self.seperator.penup()
        self.seperator.goto(0, SCREENSIZE-20)
        self.seperator.right(90)
        self.draw()

    # Drawing screen seperator in the middle of the screen
    def draw(self):
        for _ in range(SCREENSIZE, -SCREENSIZE, -40):
            self.seperator.pendown()
            self.seperator.forward(20)
            self.seperator.penup()
            self.seperator.forward(20)
