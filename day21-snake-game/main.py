from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

border_pen = Turtle()
border_pen.hideturtle()
border_pen.pencolor("red")
border_pen.penup()
border_pen.goto(-260, -260)
border_pen.pendown()
for i in range (4):
    border_pen.forward(520)
    border_pen.left(90)

snake = Snake()
food = Food()
score = ScoreBoard()

game_is_on = True

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Right", fun=snake.move_right)

score.message()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.increase_size()
    if snake.head.xcor() >= 255 or snake.head.xcor() <= -255 or \
       snake.head.ycor() >= 255 or snake.head.ycor() <= -255:
        score.game_over()
        game_is_on = False
        
    for part in snake.body_parts[1:]:
        if snake.head.distance(part) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()

