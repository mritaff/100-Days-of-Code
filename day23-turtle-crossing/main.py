import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard    

def exit_game():
    screen.bye()

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(exit_game, "Escape")

i = 0
score.display_score()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_cars()
    
    for one_car in car.all_cars:
        if one_car.distance(player) < 20:
            score.game_over()
            game_is_on = False
    
    if player.ycor() >= 280:
        player.going_home()
        score.increase_score()
        score.display_score()
        car.increase_speed()
        
screen.exitonclick()
