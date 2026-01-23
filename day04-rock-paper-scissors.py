import random

your_choice=int(input("Choose: Rock (0), Paper (1) or Scissors (2)? "))
computer_choice=random.randint(0,2)

scissors='''    
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''    
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

hands=[rock, paper, scissors]
print(f"{hands[your_choice]}")

print("\nThe computer choice is:")
print(f"{hands[computer_choice]}")

if (your_choice==0 and computer_choice==2) or (your_choice==1 and computer_choice==0) or (your_choice==2 and computer_choice==1):
    print("You win")
elif (your_choice==2 and computer_choice==0) or (your_choice==0 and computer_choice==1) or (your_choice==1 and computer_choice==2):
    print("You lose")
else:
    print("It's a draw")