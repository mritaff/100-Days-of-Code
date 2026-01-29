import os
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

options = menu.get_items()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu_validation(count):
    if count == 0:
        print("You didn't make any coffee!")
        while True:
            choice = input("Do you really want to exit? (y/n) ").lower()
            if choice == "y":
                print("So, bye, bye!")
                return True
            elif choice == "n":
                print("So, returning to menu!")
                return False
            else:
                print("Invalid choice! Please type 'y or 'n'.")
    else:
        print("Thanks for the coffee run!")
        return True

i = 0

while True:
    clear()
    choice = input(f"What would you like {options}? ").lower()
    if choice == "report":
        coffee_machine.report()
        money_machine.report()
        continue
    elif choice == "exit":
        if menu_validation(i):
            break
        else:
            input("")
            continue

    item = menu.find_drink(choice)
    if (item is not None):
        if coffee_machine.is_resource_sufficient(item):
            if money_machine.make_payment(item.cost):
                coffee_machine.make_coffee(item)
                i+=1
    
        input("")
    else:
        continue