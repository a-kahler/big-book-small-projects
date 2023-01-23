"""Forest Fire Sim, by Austii KAY
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model

"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext')
    sys.exit()

# Set up the constants 
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20 # Amount of forest that starts with trees.
GROW_CHANCE = 0.01 # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01 # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5


