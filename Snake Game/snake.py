from turtle import Turtle
STARTING_POS=[(0, 0), (-20, 0), (-40, 0)]
DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        #TODO 2:Create a snake body
        self.snake=[]
        self.create_snake()
        self.head=self.snake[0]
    def create_snake(self):
        for position in STARTING_POS:
            self.add_seg(position)
    def add_seg(self,position):
        t = Turtle("square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.snake.append(t)
    def extend(self):
        #TODO 9:Extend the body of the snake
        last_seg=self.snake[-1].position()
        self.add_seg(last_seg)
    def move(self):
        #TODO 3:Move the snake
        for seg in range(len(self.snake) - 1, 0, -1):
            x = self.snake[seg - 1].xcor()
            y = self.snake[seg - 1].ycor()
            pos = (x, y)
            self.snake[seg].goto(pos)
        self.snake[0].forward(DISTANCE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)
    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]
