from turtle import Turtle
from gamelogic import GameLogic

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.logic = GameLogic()

    def display_state(self, user_choice):
        x, y = self.logic.state_location(user_choice.lower())
        self.goto(x, y)
        self.write(f"{user_choice.capitalize()}", align="center", font=("Arial", 12, "normal"))

    def win_message(self):
        self.home()
        self.color("#00ae09")
        self.write("Congratulations! You win!", align="center", font=("Arial", 20, "normal"))