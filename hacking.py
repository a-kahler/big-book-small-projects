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


