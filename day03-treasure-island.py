print(r"""
                         ,----------_____....----.--------,
                _____.....-----~~~~~             |_______/ `
               |                                 |      /  |
               |          H E L L O              |     /
               |                                  |   /   /
                |                                 | _/   /
                |            W O R L D            |,'|~~
               ,|                                ,'  |
             ,'_|_____________________________:,' /) |.
             |  \    \                /    /  |  (/  |_. .
             |   \    \     {}       /    /   |    .' .  .
          . '|    \    \            / _  /    |    ,   .  .
         . . |\    \    \          _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .
""")
print("\nThat's Treasure Island.\nYour mission is to find the treasure.\n")
direction=input("You're need to choose a direction, left or right?")

if direction.lower()=="left":
    decision2=input("Walking on the left, you came near a river, you'll wait or swin? ")

    if decision2.lower()=="wait":
        doors=input("You wait and, magically, three door appear front of you: red, blue and yellow. Wich one you choose? ")
        
        if doors.lower()=="blue":
            print("Behind the door had a treasure!")
            print("Congratulations, you win!")
        elif doors.lower()=="red":
            print("When you touch the handle, a fireball exploded, burning you to death :)")
        elif doors.lower()=="yellow":
            print("When you entered the room, the treasure chest was there.")
            print("You runned to open it, but was struck by lightning, dying instantly :)")    
    else:
        print("You didn't notice, but the river was full of piranhas waiting for you, your end was not pleasant...")

else:
    print("You go to the right, ending up in a snakes nest.")
    print("For your misfortune, they were all venomous and territorialists.")
    print("You were attacked and died painfully...")