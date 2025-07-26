from turtle import Turtle
# TODO 3:Create ball and move it
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(1,1)
        self.x=10
        self.y=10
        self.move_speed=0.1
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    #TODO 4:Detect collision with wall
    def bounce_wall(self):
        self.y*=-1
    def bounce_paddle(self):
        self.x*=-1
        self.move_speed*=0.9
    def refresh(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_paddle()