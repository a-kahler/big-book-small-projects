"""Langton's Ant, by Austii KAY
A cellular automata animation. Press Ctrl-C to stop.
More info: https://en.wikipedia.org/wiki/Langton%27s_ant

"""

import copy, random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1
HEIGHT -= 1 # Adjustment for the quit message at the bottom.

NUMBER_OF_ANTS = 10 # (!) Try changing this to 1 or 50.
PAUSE_AMOUNT = 0.1 # (!) Try chaning this to 1.0 or 0.0.

# (!) Try changing these to make the ants look different:
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) Try changing these colors to one of 'black', 'red', 'green',
# 'yellow', 'blue', 'purple', 'cyan', or 'white'. (These are the only
# colors that the bext module supports.)
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TITLE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

