import random

NUMBER = random.randint(1, 101)

print("Welcome, to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choice = input("Choose a difficult level. Type 'easy' or 'hard': ")
if choice.lower == "easy":
    attempts = 10
elif choice.lower == "hard":
    attempts = 5
else:
    print("Invalid difficult level. Defined to hard 'hard' by default.")
    attempts = 5

while True:
    print(f"Do you have {attempts} remaining attempts.")
    guess = int(input("Make a guess: "))

    if guess < NUMBER:
        print("The guess was low.\n")
        attempts -= 1
    elif guess > NUMBER:
        print("The guess was high.\n")
        attempts -= 1
    else:
        print(f"Congratulations! You guessed the number {NUMBER} correctly!")
        break

    if attempts == 0:
        print(f"Your attempts are over. The number was {NUMBER}.")
        break