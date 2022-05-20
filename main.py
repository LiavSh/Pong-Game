from scoreline import ScoreLine
from screen import MyScreen
from paddle import CreatePaddle
from ball import Ball
import time

# Selection cords for the paddles and the secondary color of the game
left_pos = (-560, 0)
right_pos = (560, 0)
right_scoreline = (320, 350)
left_scoreline = (-320, 350)
color = "purple"

# setting up the game (screen / paddles)
game_screen = MyScreen()
left_paddle = CreatePaddle(left_pos, color)
right_pedal = CreatePaddle(right_pos, color)
lft_score_line = ScoreLine(left_scoreline, color)
rgt_score_line = ScoreLine(right_scoreline, color)

# Assigning control keys
game_screen.screen.listen()
game_screen.screen.onkey(left_paddle.go_up, "a")
game_screen.screen.onkey(left_paddle.go_down, "z")
game_screen.screen.onkey(right_pedal.go_up, "Up")
game_screen.screen.onkey(right_pedal.go_down, "Down")

# Creating the ball for the game
game_ball = Ball()
game_on = True


while game_on:
    game_screen.screen.update()
    time.sleep(game_ball.move_speed)
    game_ball.move_forward()
    game_ball.wall_reflect()
    game_ball.pad_touch(left_paddle)
    game_ball.pad_touch(right_pedal)
    res = game_ball.out_of_boundary()
    if res == "right":
        lft_score_line.add_score()
        game_ball.restart_game()
    elif res == "left":
        rgt_score_line.add_score()
        game_ball.restart_game()

game_screen.screen.exitonclick()
