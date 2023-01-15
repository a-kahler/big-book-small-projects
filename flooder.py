"""Flooder, by Austii KAY
A colorful game where you try to fill the board with a single color. Has
a mode for colorblind players.
Inspired by the "Flood Itl" game.

"""

import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext')
    sys.exit()

# Set up the constants:
