"""Hacking Minigame, by Austii KAY
The hacking mini-game from "Fallout 3". Find out which seven-letter
word is the password by using clues each guess gives you.

"""

# NOTE: This program requires the sevenletterwords.txt file. You can
# download it from https://inventwithpython.com/sevenletterwords.txt

import random, sys

# Set up the constants:
# The garbage filler characters for the "computer memory" display.
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

# Load the WORDS list from a text file that has 7-letter words.
with open('sevenletterwords.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range(len(WORDS)):
    # Convert each word to uppercase and remove the trailing newline:
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """Run a single game of Hacking."""
    print('''Hacking Minigame, by Austii KAY
    Find the password in the computer's memory. You are given clues after
    each guess. For example, if the secret password is MONITOR but the
    player guessed CONTAIN, they are given the hint that 2 out of 7 letters
    were correct, because both MONITOR and CONTAIN have the letter O and N
    as their 2nd and 3rd letter. You get four guesses./n''')
    input('Press Enter to begin...')

    gameWords = getWords()
    # The "computer memory" is just cosmetic, but it looks cool:
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    # Start at 4 tries remaining, going down:
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('A C C E S S  G R A N T E D')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
    print('Out of tries. Secret password was {}.'.format(secretPassword))


def getWords():
    """Return a list of 12 words that could possibly be the password.
    
    The secret password will be the first word in the list.
    To make the game fair, we try to ensure that there are words with
    a range of matching numbers of letters as the secret word."""
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    # Find two more words; these have zero matching letters.
    # We use "< 3" because the secret password is already in words.
    while len(words) < 3:
        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 0:
            words.append(randomWord)

    # Find two words that have 3 matching letters (but give up at 500
    # tries if not enough can be found).
    for i in range(500):
        if len(words) == 5:
            break # Found 5 words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) == 3:
            words.append(randomWord)
    
    # Find at least seven words that have at least one matching letter
    # (but give up at 500 tries if not enough can be found).
    for i in range(500):
        if len(words) == 12:
            break # Found 7 or more words, so break out of the loop.

        randomWord = getOneWordExcept(words)
        if numMatchingLetters(secretPassword, randomWord) != 0:
            words.append(randomWord)
    
    # Add any random words needed to get 12 words total.
    while len(words) < 12:
        randomWord = getOneWordExcept(words)
        words.append(randomWord)

    assert len(words) == 12
    return words


