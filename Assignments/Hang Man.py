import random
from shutil import which

words = ["sanaa", "taiz", "aden", "hadhramot", "mareb", "hodaida", "socatra"]
randWord = random.choice(words)
guessedLetters = []
tries = 4
Counter = 1
while tries > 0 :
    guessed_word = ""
    for letter in randWord:
            if letter in guessedLetters:
                guessed_word += letter
            else:
                guessed_word += "_"

    if guessed_word == randWord:
            print("\n\n Correct answer , you win ^_^ \n\n")
            break

    print(guessed_word)

    letter = input(f"\n Enter letter {Counter} :  ").lower()

    if len(letter) != 1:
            print(" \n You have to enter one letter, please !")
            continue



    if letter in guessedLetters:
            print("\n This letter had entered before, choose another one !")

    elif letter in randWord:
            guessedLetters.append(letter)
            print("\n Correct letter!")
            
    else:
            tries -= 1
            print(f" \n Wrong, you still have {tries} tries.")
    Counter += 1     

if tries == 0:
    print(f" \n\n\n Wrong ! \nThe correct answer was : {randWord}\n\n ")

