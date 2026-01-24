import random

word_list=["pretinha", "bentinho", "janja", "perola", "cat", "dog", "geraldo", "lily", "adelaide"]
choice=random.randint(0, len(word_list)-1)
word_game=word_list[choice]
blanket_space=len(word_game)
display=["_"]*blanket_space
words_tried=[]

for i in range(0, blanket_space):
    display[i]="_"

display_str=" ".join(display)

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/          \n''')

print(f"{display_str}\n")

j=6
choice=0

while j>0:

    guess=input("Guess a letter of word! ").lower()

    correct_answer=False

    if guess in words_tried:
        print("That letter was used, try another!\n")
    else:

        for k in range(0, blanket_space):
            if word_game[k]==guess:
                display[k]=guess
                correct_answer=True
                choice+=1
        
        display_str=" ".join(display)

        if not correct_answer:
            j-=1

        print(f"{display_str}\n")
        
        print(f"Number of remaing body parts is: {j}\n")
        
        if choice==blanket_space:
            break

    words_tried.append(guess)

if j==0:
    print("You lost!")
elif j>0:
    print("You win!")

print(f"The word was: {word_game}") 