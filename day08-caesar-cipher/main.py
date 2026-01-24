alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(shift, text, alphabet):
    result=""
    
    for letter in text:

        if letter in alphabet:
            new_index=alphabet.index(letter)
            current_index=(new_index+shift)%26
            result=result+alphabet[current_index]
        else:
            result=result+letter

    return result

def decrypt(shift, text, alphabet):
    result=""
    
    for letter in text:

        if letter in alphabet:
            new_index=alphabet.index(letter)
            current_index=(new_index-shift)%26
            result=result+alphabet[current_index]
        else:
            result=result+letter

    return result

direction=input("Type 'code' to encrypt or 'decode' to decrypt\n").lower()

if direction=="code":
    text=input("Type your message: \n").lower()
    shift=int(input("Type a number of displaced houses: \n"))
    encode=encrypt(shift, text, alphabet)
    print(f"{encode}")
elif direction=="decode":
    text=input("Type your message: \n").lower()
    shift=int(input("Type a number of displaced houses: \n"))
    decode=decrypt(shift, text, alphabet)
    print(f"{decode}")
else:
    print("ERROR: invalid option!")