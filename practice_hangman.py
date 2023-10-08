# Write a Python program to play a simplified version of the game hangman. Have User 1 input a
# secret word with a minimum length of 6. Then, take as input from User 2 one letter at a time until
# they guess a letter that is not in the secret word. At the end of the program, print out the number of
# guesses and the secret word.

secret = input("Enter the secret word:")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
original = secret

ogkey = set()
key = set()
set = set()
count = 0
lives=6
secret=secret.lower()
#print(secret)
secret = list(secret)
empty=[]
for i in range(len(secret)):
    empty.append("_")

if len(secret) < 6:
    print("please enter a valid input")
    exit()
for i in secret:
    key.add(i)
    ogkey.add(i)

def print_hangman(letter):
    for i in range(len(secret)):
        if secret[i]==letter:
            empty[i]=letter
    print(" ".join(empty))


guess = True
letter = (input("Guess a letter:")).lower()
if letter in key:
    key.remove(letter)
    count += 1
    #print(key,set)
    print_hangman(letter)
elif letter in ogkey:
    print("you already guessed this letter")
else:
    lives=lives-1
    print(f"Wrong guess you now have {lives} lives")
count += 1

while lives!=0 and key != set:
    letter = (input("Guess another letter:")).lower()
    if letter in key:
        key.remove(letter)
        #print(key,set)
        print_hangman(letter)
    elif letter in ogkey:
        print("you already guessed this letter")
    else:
        lives=lives-1
        print(f"Wrong guess you now have {lives} lives")
    count += 1

print(key==set)
if key == set:
    print(f'The secret word is: "{original}". You found it in {count} guesses!')
else:
    print(f'The secret word is: "{original}". You took {count} guesses!')
