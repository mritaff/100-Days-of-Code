import random
import os
import game_data
import art

def get_random_account():
    return random.choice(game_data.data)

def comparator(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        higher = account_a["follower_count"]
    elif account_a["follower_count"] < account_b["follower_count"]:
        higher = account_b["follower_count"]
    return higher

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

score = 0

account_a = get_random_account()
account_b = get_random_account()

print(art.logo)

while True:
    while account_a == account_b or account_a["follower_count"] == account_b["follower_count"] :
        account_b = get_random_account()

    higher = comparator(account_a, account_b)

    print(f"Compare A: {account_a["name"]}, {account_a["description"]} from {account_a["country"]}")
    print(art.vs)
    print(f"Against B: {account_b["name"]}, {account_b["description"]} from {account_b["country"]}")

    choice = input("Who has more followers 'A' or 'B'? ")

    clear()

    print(art.logo)

    if choice.upper() == 'A' and higher == account_a["follower_count"]:
        score+=1
        print(f"You're right! Current score: {score}")
        account_a = account_b
    elif choice.upper() == 'B' and higher == account_b["follower_count"]:
        score+=1
        print(f"You're right! Current score: {score}")
        account_a = account_b
    else:
        print(art.game_over)
        print(f"You were wrong! Current score: {score}")
        break

    account_b = get_random_account()