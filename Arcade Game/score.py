#TODO 7:Maintaining the score
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_board()
    def score_board(self):
        self.goto(-100, 200)
        self.write(self.score1, False, "center", ("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.score2, False, "center", ("Courier", 70, "normal"))
    def update_score1(self):
        self.score1+=1
        self.clear()
        self.score_board()
    def update_score2(self):
        self.score2 += 1
        self.clear()
        self.score_board()