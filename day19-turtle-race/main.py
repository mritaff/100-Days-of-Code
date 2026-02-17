from turtle import Turtle, Screen
from race_logic import TurtleRace

is_race_over = False

screen = Screen()
screen.setup(1280, 720)
screen.title("Turtle Race")

race = TurtleRace()

user_bet = ""

while user_bet.lower() not in race.colors:
    user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color: ")
    if user_bet is None:
        break
    
if user_bet:
    winner, is_race_over = race.running()
    
    if is_race_over:
        race.results(winner, user_bet)

screen.exitonclick()
