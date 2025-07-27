import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#TODO 1:Setup the screen
screen = Screen()
screen.title("My Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car=CarManager()
score=Scoreboard()
screen.listen()
screen.onkey(fun=player.move_up,key="Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move_car()
    #TODO 4:Detect collision with car
    for cars in car.all_cars:
        if player.distance(cars)<20:
            score.game_over()
            game_is_on=False
    #TODO 5:Detect collision with finish line and increase speed
    if player.finish_line():
        score.update()
        car.move_speed()
        player.refresh()
screen.exitonclick()