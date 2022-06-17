import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move_up, "Up")

scoreboard.write_level()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.add_car()
    car_manager.move_cars(scoreboard.level)

    # Detect collision with the car
    for car in car_manager.car_set:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.ycor() >= 280:
        scoreboard.level_up()
        player.reset_position()
        scoreboard.write_level()
        car_manager.rdm_parameter *= 0.90
    screen.update()

screen.exitonclick()
