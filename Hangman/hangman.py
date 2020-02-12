import random

def get_word():
    WORDS = ("python", "jumble", "easy", "difficult", "answer",  "xylophone",'computer','Apple','Simmer')
    word = random.choice(WORDS)
    return word

def display_string(string_array):
    string = ''
    for letter in string_array:
        string += letter +' '
    return string

word = get_word()
my_string = ["_"]*len(word)
number_of_guesses = 8
guess_count = 0
word_count = len(word)
print()
print("======Welcome to Hangman!======")

while (guess_count < number_of_guesses) and (word_count != 0):
    print(f"The word now looks like this {display_string(my_string)}")
    print(f"You have {number_of_guesses - guess_count} guesses left.")
    print()
    guess = input("Your guess: ")
    i = 0
    found = 0

    while i < len(word):
        if guess.lower() == word[i].lower():
            if my_string[i] == "_":
                my_string[i] = word[i]
                found = 1
                break
        i += 1
    
    if found == 0:
        print(f"There are no {guess}'s in the word.")
        print()
        guess_count += 1
    else:
        print("Correct!")
        print()
        word_count -= 1

if guess_count == number_of_guesses:
    print("Out of guesses!\nYou have been hanged :(")

else:
    print()
    print("=======YOU GUESSED THE WORD!!=========")
    print(display_string(my_string))
    print()













