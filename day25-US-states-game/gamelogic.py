import pandas as pd

class GameLogic:
    def __init__(self):
        self.score = 0
        self.data = pd.read_csv("brazilian_states.csv")
        self.options = self.data["state"].tolist()
        self.choices = []
    
    def answers (self, user_input):
        self.choices.append(user_input)

    def state_location(self, user_input):
        state = self.data.loc[self.data["state"] == user_input]
        x = int(state["x"].values[0])
        y = int(state["y"].values[0])

        return x, y
    def increase_score(self):
        self.score += 1