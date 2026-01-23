import random

def create_deck():
    values = {"Ace": 11,
              "1": 1,
              "2": 2, 
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
              "10": 10,
              "Jack": 10,
              "Queen": 10,
              "King": 10}
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    deck = {}

    for suit in suits:
        for card, value in values.items():
            key = f"{card} {suit}"
            deck[key] = value

    return deck

# Draw a random card
def hand(deck):
    keys = list(deck.keys())
    card_draw = random.choice(keys)
    value = deck[card_draw]

    return card_draw, value

# Handle the player's turn
def player(cards_player, score_player, cards_played, deck):
    card, value = hand(deck)
    if card not in cards_played:
        cards_player.append(card)
        cards_played.append(card)
        score_player += value

        return cards_player, score_player, cards_played
    else:
        return player(cards_player, score_player, cards_played, deck)

# Handle the computer's turn
def machine(cards_pc, score_pc, cards_played, deck):
    card, value = hand(deck)
    if card not in cards_played:
        cards_pc.append(card)
        cards_played.append(card)
        score_pc += value
        return cards_pc, score_pc, cards_played
    else:
        return machine (cards_pc, score_pc, cards_played, deck)
    
# Display the game result
def status (score_pc, score_player):
    if (score_pc == score_player) and (score_pc <= 21 and score_player <= 21):
        print("You tied\n")
    elif ((score_pc < score_player) and score_player <= 21) or score_pc > 21:
        print("You won\n")
    else:
        print("You lost\n")

# Create a deck for the game
deck = create_deck()

while True:
    cards_played = []
    cards_pc = []
    cards_player = []
    score_pc = 0
    score_player = 0
    i = 0

    choice = input("Do you want to play blackjack? (y/n) ")

    if choice.lower() == "n":
        break

    choice2 = "null"

    print("\n")

    while True:
        
        if i >= 2 and choice2.lower() != "n":
            choice2 = input("Do you want to draw another card? (y/n) ")

        if i < 2 or choice2.lower() == "y":
            cards_player, score_player, cards_played = player(cards_player, score_player, cards_played, deck)

        if score_pc < 16:
            cards_pc, score_pc, cards_played = machine(cards_pc, score_pc, cards_played, deck)
        
        if i >= 1:
            print(f"Cards played by you: {cards_player}\nYour score: {score_player}")
            print(f"Cards played by machine: {cards_pc}\nMachine's score: {score_pc}")
            print("\n")

        if (score_pc >= 16 and choice2 == "n") or (score_pc >= 21 or score_player >= 21):
            break

        i+=1

    status(score_pc, score_player)