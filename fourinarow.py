"""Four in a Row, by Austii KAY
A tile-dropping game to get four in a row, similar to Connect Four.

"""

import sys

# Constants used for displaying the board:
EMPTY_SPACE = '.' # A period is easier to count than a space.
PLAYER_X = 'X'
PLAYER_O = 'O'

# Note: Update displayBoard() & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


