from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(.75, .75)
        self.y_move = 10
        self.x_move = 10
        self.spd = .1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.y_move *= -1

    def hit_paddle(self, paddle):
        if self.distance(paddle) < 50 and self.xcor() > 325 or self.distance(paddle) < 50 and self.xcor() < -325:
            self.x_move *= -1
            self.spd *= .9

    def reverse_direction(self):
        self.x_move *= -1
