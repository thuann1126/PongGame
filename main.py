import turtle
from ball import Ball
from scoreBoard import ScoreBoard
from paddle import Paddle
from aiPaddle import AiPaddle
from turtle import Screen, Turtle

#Objects setup
screen = Screen()
#Skip the setup animation
screen.tracer(0)
drawer = Turtle()
p = Paddle()
ai = AiPaddle()
ball = Ball()
sb = ScoreBoard()



#Initialize the pen
drawer.color("white")
drawer.pensize(5)

# Set up the screen
screen.setup(1000, 800)
turtle.colormode(255)
turtle.hideturtle()
screen.bgcolor(141, 255, 54)

#Draw the pong table
#Draw the upper line
drawer.penup()
drawer.goto(-500, 350)
drawer.pendown()
drawer.forward(1000)
#Draw the side divided line
drawer.penup()
drawer.goto(0, 350)
drawer.pendown()
drawer.setheading(270)
drawer.forward(750)
#Draw the center dot
drawer.penup()
drawer.goto(0, 0)
drawer.pendown()
drawer.dot(50)
#Draw the center circle
drawer.penup()
drawer.goto(-200, 0)
drawer.pendown()
drawer.circle(200)
drawer.hideturtle()


#screen even listener
screen.listen()
screen.onkey(p.up, "Up")
screen.onkey(p.down, "Down")
screen.onkeypress(p.up, "Up")
screen.onkeypress(p.down, "Down")

#Start to capture the animation
game_is_on = True


while game_is_on:
    screen.update()

    ball.spawn_ball_to_player()

    if ball.is_player_paddle_colission(p.xcor(), p.ycor()) == False:
        sb.ai_score += 1
        ball.resetBall()
        ball.x_direction = -ball.x_direction
        ball.spawn_ball_to_player()


    if ball.is_ai_paddle_colission(ai.xcor(), ai.ycor()) == False:
        sb.player_score += 1
        ball.resetBall()
        ball.x_direction = -ball.x_direction
        ball.spawn_ball_to_ai()

    sb.draw_score_board()
    ai.move()

#Screen event listener



screen.exitonclick()