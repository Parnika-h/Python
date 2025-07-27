from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
#TODO 2:Create and move the turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.refresh()
        self.setheading(90)
    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def refresh(self):
        self.goto(STARTING_POSITION)
    def finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False