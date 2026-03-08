from turtle import Turtle, Screen
from gamelogic import GameLogic
from text import Text

def exit_game():
    screen.bye()

IMAGE = "Brazil_blank_states.gif"

screen = Screen()
screen.title("Brazilian Game")

message = Text()
brazil_map = Turtle()
logic = GameLogic()

screen.addshape(IMAGE)
brazil_map.shape(IMAGE)

screen.listen()
screen.onkey(key="Escape", fun=exit_game)

game_is_on = True
while game_is_on:
    user_choice = screen.textinput(f"{logic.score}/27", "Type a state!")
    
    if user_choice.lower() == "exit":
        exit_game()
    
    if user_choice.lower() in logic.options and user_choice.lower() in logic.choices:
        continue
    
    if user_choice.lower() in logic.options:
        logic.increase_score()
        logic.answers(user_choice.lower())
        message.display_state(user_choice.capitalize())

    if logic.score == 27:
        message.win_message()
        game_is_on = False

screen.exitonclick()