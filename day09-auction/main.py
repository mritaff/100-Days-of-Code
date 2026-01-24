import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def bidders(name, bid):
    bet.append({
            "name":name,
            "deal":bid
        })

def higher(bet):
    int_bet=[]
    nicks=[]

    for item in bet:
        
        if item["deal"][0]=='$':
            item["deal"]=item["deal"][1:]
        
        int_bet.append(int(item["deal"]))
        nicks.append(item["name"])

    higher=int_bet[0]
    higher_name=nicks[0]

    for i in range(len(int_bet)):
        if int_bet[i]>higher:
            higher=int_bet[i]
            higher_name=nicks[i]

    return higher_name, higher

bet=[]

while 1:
    name=input("What's your name? ")
    bid=input("What's your bid? $")

    bidders(name, bid)

    choice=input("Are there other bettors?(yes/no) ").lower()

    if choice== "no":
        break
    
    os.system("clear")

winner, value=higher(bet)

clear()

print(f"The winner is {winner} with ${value}")