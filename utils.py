import string


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def isWordGuessed(secretWord, lettersGuessed):
    for word in secretWord:
        if word not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    word = ""
    for char in secretWord:
        if char in lettersGuessed:
            word = word + char
        else:
            word = word + "_ "
    return word


def getAvailableLetters(lettersGuessed):
    remain = ""
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            remain += char
    return (remain)
