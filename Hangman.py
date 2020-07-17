import random
from utils import *


def hangman(secretWord):
    num = 8
    lettersGuessed = []

    print(bcolors.HEADER + "***** Welcome to the Hangman game ***** \n" + bcolors.ENDC)
    print("I am thinking of a word which is " + str(len(secretWord)) + " letters long.")

    while (num > 0):
        print("\nYou have " + str(num) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed), '\n')
        print("Please guess a letter: ", end='')

        guessInLowerCase = input().lower()

        if guessInLowerCase in secretWord and guessInLowerCase not in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
            print(bcolors.OKGREEN + 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed) + bcolors.ENDC)
        elif guessInLowerCase in lettersGuessed:
            print(bcolors.WARNING + "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed) + bcolors.ENDC)
        else:
            lettersGuessed.append(guessInLowerCase)
            print(bcolors.WARNING + 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed) + bcolors.ENDC)
            num -= 1

        if isWordGuessed(secretWord, lettersGuessed):
            print(bcolors.OKGREEN + '***** Congratulations! You won! *****' + bcolors.ENDC)
            break

    if not (isWordGuessed(secretWord, lettersGuessed)):
        print(bcolors.FAIL + 'Sorry, you ran out of guesses. The word was ' + secretWord + bcolors.ENDC)


if __name__ == "__main__":
    words = open('words.txt', 'r').readline().split()
    secretWord = random.choice(words).lower()
    hangman(secretWord)
