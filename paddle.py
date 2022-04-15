from turtle import Turtle

PLAYER_PADDLE_POSITION = (-490, 0)
TOP_RANGE =  300
BOT_RANGE = -330
GO_UP = 90
GO_DOWN = 270

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square") #Default 20x20
        self.shapesize(1, 4)
        self.setheading(90)
        self.penup()
        self.goto(PLAYER_PADDLE_POSITION)
        self.speed("fastest")

    def up(self):
        if self.ycor() < TOP_RANGE :
            self.setheading(GO_UP)
            self.forward(30)

    def down(self):
        if self.ycor() > BOT_RANGE :
            self.setheading(GO_DOWN)
            self.forward(30)
