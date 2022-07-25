from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.goto(x = 0, y = 290)
        self.color("white")
        self.write(f"{self.l_score}            {self.r_score}", align=ALIGNMENT, font = FONT)

    def update_scoreboard(self, ball):
        if ball.xcor() == 370:
            self.clear()
            self.l_score += 1
            self.write(f"{self.l_score}      {self.r_score}", align=ALIGNMENT, font=FONT)
            ball.goto(0, 0)
            ball.reverse_direction()
            ball.spd = .1
        if ball.xcor() == -350:
            self.clear()
            self.r_score += 1
            self.write(f"{self.l_score}      {self.r_score}", align=ALIGNMENT, font=FONT)
            ball.goto(0, 0)
            ball.reverse_direction()
            ball.spd = .1

