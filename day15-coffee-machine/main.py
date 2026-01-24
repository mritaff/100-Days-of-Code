MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def missing_resources(drink, resources):
    missing = []
    for ingredients, amount in drink["ingredients"].items():
        if amount > resources[ingredients]:
            missing.append(ingredients)
    
    return missing

def payment(quarters, dimes, nickles, pennies, total):
    value = pennies * 0.01 + nickles * 0.05 + dimes * 0.10 + quarters * 0.25
    if value >= total:
        return value - total
    else:
        return False

while True:
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in MENU:
        drink = MENU[choice]
        invalid = missing_resources(drink, resources)

        if len(invalid) > 0:
            if len(invalid) == 1:
                print(f"Sorry, but the machine doesn't have {invalid[0]} enough.")
            else:
                items = ", ".join(invalid[:-1])
                print(f"Sorry, but the machine doesn't have {items} and {invalid[-1]} enough.")

        else:
            print("Please, insert the coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            change = payment(quarters, dimes, nickles, pennies, total=drink["cost"])
            if change == False:
                print("Sorry that's not enough money. Money refunded")
            else:
                print(f"Here is {change: .2f} in change.")
                print(f"Here is your {choice}. Enjoy!")
                resources["water"] -= drink["ingredients"]["water"]
                for ingredients, amount in drink["ingredients"].items():
                    resources[ingredients] -= amount
                resources["money"] += drink["cost"]

    elif choice == "report":
        for resource in resources:
            if resource == "coffee":
                print(f"{resource}: {resources[resource]}g")
            elif resource == "money":
                print(f"{resource}: ${resources[resource]}")
            else:
                print(f"{resource}: {resources[resource]}ml")
    elif choice == "exit":
        break
    else:
        print("Invalid choice.")
