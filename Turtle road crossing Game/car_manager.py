import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#TODO 3:Create and move the cars
class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create(self):
        chance=random.randint(1,6)
        if chance==1:
            car=Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            y=random.randint(-250,250)
            car.goto(300,y)
            car.setheading(180)
            self.all_cars.append(car)
    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    def move_speed(self):
        self.car_speed+=MOVE_INCREMENT

