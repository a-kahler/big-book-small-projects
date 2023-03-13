"""Hourglass, by Austii KAY
An animation of an hourglass with falling sand. Press Ctrl-C to stop.

"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
PAUSE_LENGTH = 0.2 # (!) Try changing this to 0.0 or 1.0.
# (!) Try changing this to any number between 0 and 100:
WIDE_FALL_CHANCE = 50

SCREEN_WIDTH = 79
SCREEN_HEIGHT = 25
X = 0 # The index of X values in an (x, y) tuple is 0.
Y = 1 # The index of Y values in an (x, y) tuple is 1.
SAND = chr(9617)
WALL = chr(9608)

