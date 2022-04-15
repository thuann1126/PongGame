from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ai_score = 0
        self.player_score = 0
        self.speed("fastest")



    def draw_score_board(self):
        self.clear()
        self.penup()
        self.goto(-480,350)
        self.write(f"Score: {self.player_score}", font=("Arial", 25 , "bold"))
        self.goto(350, 350)
        self.write(f"Score: {self.ai_score}", font=("Arial", 25 , "bold"))
        self.hideturtle()


