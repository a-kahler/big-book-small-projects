"""Hungry Robots, by Austii KAY
Escape the hungry robots by making them crash into each other.

"""

import random, sys

# Set up constants:
WIDTH = 40
HEIGHT = 20
NUM_ROBOTS = 10
NUM_TELEPORTS = 2
NUM_DEAD_ROBOTS = 2
NUM_WALLS = 100

EMPTY_SPACE = ' '
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'

# (!) Try changing this to '#' or '0' or ' ':
WALL = chr(9617)


