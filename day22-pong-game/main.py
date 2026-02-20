from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from decoration import Decoration
import time

def exit_game():
    screen.bye()

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

decoration = Decoration()
paddle_one = Paddle(-1)
paddle_two = Paddle(1)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle_one.move_up, "Up")
screen.onkey(paddle_one.move_down, "Down")
screen.onkey(paddle_two.move_up, "W")
screen.onkey(paddle_two.move_down, "S")
screen.onkey(paddle_two.move_up, "w")
screen.onkey(paddle_two.move_down, "s")
screen.onkey(exit_game, "Escape")

game_is_on = True
score.display_score()

while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(paddle_one) < 50 and ball.xcor() < -320):
        if ball.x_move < 0:
            ball.bounce_x()
            
    if (ball.distance(paddle_two) < 50 and ball.xcor() > 320):
        if ball.x_move > 0:
            ball.bounce_x()
        
    if ball.xcor() > 380:
        score.increase_score_one()
        score.display_score()
        ball.returning_center()
    
    if ball.xcor() < -380:
        score.increase_score_two()
        score.display_score()
        ball.returning_center()