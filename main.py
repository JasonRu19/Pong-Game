from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()

turtle = Turtle()
screen.title("Pong")
screen.screensize(600, 600)
screen.bgcolor("black")
screen.tracer(0)
score = Score()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
l_paddle.move()
r_paddle.move()

ball= Ball()

game_on = True
while game_on:
    time.sleep(ball.spd)
    screen.update()
    ball.move()
    ball.bounce()
    ball.hit_paddle(r_paddle)
    ball.hit_paddle(l_paddle)
    score.update_scoreboard(ball)
    if score.l_score == 5 or score.r_score == 5:
        game_on = False
        if score.l_score > score.r_score:
            turtle.hideturtle()
            turtle.goto(0, 0)
            turtle.color("white")
            turtle.write(f"Left Player Wins!", align="center", font=("Arial", 16, "normal"))
        else:
            turtle.hideturtle()
            turtle.goto(0, 0)
            turtle.color("white")
            turtle.write(f"Right Player Wins!", align="center", font=("Arial", 16, "normal"))


screen.exitonclick()
