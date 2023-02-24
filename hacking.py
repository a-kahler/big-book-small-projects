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
