#TODO : The Snake Game
import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
#TODO 1:Setup the screen
screen=Screen()
screen.setup(600,600)
screen.title("My Snake Game")
screen.bgcolor("Black")
screen.tracer(0)
s=Snake()
f=Food()
#TODO 4:Control the snake
screen.listen()
screen.onkey(key="Up",fun=s.up)
screen.onkey(key="Down",fun=s.down)
screen.onkey(key="Left",fun=s.left)
screen.onkey(key="Right",fun=s.right)
game_is_on=True
score=Score()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()
    # TODO 6:Detect collision with food
    if s.head.distance(f)<15:
        score.increase_score()
        s.extend()
        f.refresh()
    #TODO 8:Detect collision with wall
    x_cor=s.head.xcor()
    y_cor=s.head.ycor()
    if x_cor>=295 or y_cor>=295 or x_cor<=-295 or y_cor<=-295:
        score.reset()
        s.reset()
    #TODO 10:Detect collision with tail
    for i in s.snake[1:]:
        if s.head.distance(i)<10 and i!=s.head:
            score.reset()
            s.reset()
screen.exitonclick()
