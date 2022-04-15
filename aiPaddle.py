from turtle import Turtle

AI_PADDLE_POSITION = (490, 0)
TOP_RANGE =  250
BOT_RANGE = -330
UP = 90
DOWN = 270

class AiPaddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(2, 10)
        self.setheading(90)
        self.penup()
        self.goto(AI_PADDLE_POSITION)
        self.angle = 90



    def checkTopBotColission(self):

        if self.ycor() > TOP_RANGE:
            self.angle = 270

        elif self.ycor() < BOT_RANGE:
            self.angle = 90

    def move(self):
        self.checkTopBotColission()
        self.speed(1)
        self.setheading(self.angle)
        self.forward(5)
