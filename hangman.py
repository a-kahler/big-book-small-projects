"""Hangman, by Austii KAY
Guess the letters to a secret word before the hangman is drawn.

"""

# A version of this game is featured in the book "Invent Your Own
# Computer Games with Python" https://nostarch.com/inventwithpython

import random, sys

# Set up the constants:
# (!) Try adding or changing the strings in HANGMAN_PICS to make a 
# guillotine instaed of a gallows.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# (!) Try replacing CATEGORY and WORDS with new strings.