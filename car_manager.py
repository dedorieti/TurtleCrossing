from turtle import Turtle
import random as rdm

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_set = []
        self.rdm_parameter = 0.9

    def add_car(self):
        if rdm.random() > self.rdm_parameter:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.setheading(180)
            new_car.color(rdm.choice(COLORS))
            random_y = rdm.randint(-250, 250)
            new_car.goto(x=280, y=random_y)
            self.car_set.append(new_car)

    def move_cars(self, level):
        for car in self.car_set:
            car.forward(STARTING_MOVE_DISTANCE + level*MOVE_INCREMENT)
