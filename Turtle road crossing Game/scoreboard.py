#TODO 6:Create and maintain Level
from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-260,250)
        self.write(f"Level : {self.level}",False,"left",FONT)
    def update(self):
        self.level+=1
        self.clear()
        self.goto(-260, 250)
        self.write(f"Level : {self.level}", False, "left", FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.",False,"center",FONT)