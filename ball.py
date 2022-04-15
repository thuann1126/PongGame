import random
from turtle import Turtle

SPEED = 50
DEFAULT_POSITION = (0,0)
TOP_RANGE =  350
BOT_RANGE = -390
SPEED = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(DEFAULT_POSITION)
        self.ball_x = 0
        self.ball_y = 0
        self.x_direction = 3
        self.y_direction = 1



    def is_top_bottom_colission(self):
        if self.ball_y > TOP_RANGE or self.ball_y < BOT_RANGE:
            self.y_direction = -self.y_direction


    def is_ai_paddle_colission(self, paddle_x, paddle_y):
        if (self.xcor() == paddle_x) and (self.ycor() < paddle_y +100) and (self.ycor() > paddle_y-100):
            self.x_direction = -self.x_direction
            print(self.xcor())
            print (self.ycor())
            return True
        if (self.xcor() > paddle_x):

            return False

    def is_player_paddle_colission(self, paddle_x, paddle_y):
        if (self.xcor() == paddle_x) and (self.ycor() < paddle_y +40) and (self.ycor() > paddle_y-40):
            self.x_direction = -self.x_direction
            print(self.xcor())
            print (self.ycor())
            return True
        if (self.xcor() < paddle_x):
            return False

    def spawn_ball_to_ai(self):

            self.is_top_bottom_colission()
            self.ball_x += SPEED  * self.x_direction
            self.ball_y += SPEED * self.y_direction
            self.goto(self.ball_x, self.ball_y)

    def spawn_ball_to_player(self):

        self.is_top_bottom_colission()
        self.ball_x += SPEED * -self.x_direction
        self.ball_y += SPEED  * self.y_direction
        self.goto(self.ball_x, self.ball_y)

    def resetBall(self):
        self.ball_x = 0
        self.ball_y = 0




