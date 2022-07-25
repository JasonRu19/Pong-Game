from turtle import Turtle, Screen
LEFT_POS = (-350, 0)
RIGHT_POS = (350, 0)


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position)
        self.screen = Screen()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move(self):
        self.screen.listen()
        if self.position == LEFT_POS:
            self.screen.onkey(self.move_up, "w")
            self.screen.onkey(self.move_down, "s")
        else:
            self.screen.onkey(self.move_up, "Up")
            self.screen.onkey(self.move_down, "Down")
