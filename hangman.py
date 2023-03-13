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
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


def main():
    print('Hangman, by Austii KAY')

    # Setup variables for a new game:
    missedLetters = [] # List incorrect letter guesses.
    correctLetters = [] # List of correct letter guesses.
    secretWord = random.choice(WORDS) # The word the player must guess.

    while True: # Main game loop.
        drawHangman(missedLetters, correctLetters, secretWord)

        # Let the player enter their letter guess:
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # Add the correct guess to correctLetters:
            correctLetters.append(guess)

            # Check if the player has won:
            foundAllLetters = True # Start off assuming they've won.
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # There's a letter in the secret word that isn't
                    # yet in correctLetters, so the player hasn't won:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break # Break out of the main game loop.
        else:
            # The player has guessed incorrectly:
            missedLetters.append(guess)

            # Check if the player has guessed too many times and lost. (The
            # "- 1" is because we don't count the empty gallows in
            # HANGMAN_PICS.)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break


