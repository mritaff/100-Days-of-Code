from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
        
snake = Snake()

game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
