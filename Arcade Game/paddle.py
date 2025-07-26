from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5,1)
        self.goto(self.x,self.y)
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.x, new_y)
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.x, new_y)
