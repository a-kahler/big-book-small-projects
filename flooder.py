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
BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

# Constants for the different shapes used in colorblind mode:
HEART       = chr(9829)
DIAMOND     = chr(9830)
SPADE       = chr(9824)
CLUB        = chr(9827)
BALL        = chr(9679)
TRIANGLE    = chr(9650)

BLOCK       = chr(9608)
LEFTRIGHT   = chr(9472)
UPDOWN      = chr(9474)
DOWNRIGHT   = chr(9484)
DOWNLEFT    = chr(9488)
UPRIGHT     = chr(9492)
UPLEFT      = chr(9496)
# A list of chr() codes is at https://inventwithpython.com/chr

# All the color/shape tiles used on the board:
TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue',
                3:'yellow', 4: 'cyan', 5: 'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND,
              3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('''Flooder, by Austii KAY

Set the upper left color/shape, which fills in all the
adjacent squares of that color/shape. Try to make the
entire board the same color/shape.''')

    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE
    
    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True: # Main game loop.
        displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break

    
def getNewBoard():
    """Return a dictionary of a new Flood It board."""

    # Keys are (x, y) tuples, values are the tile at that position.
    board = {}

    # Create random colors for the board.
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    # Make several tiles the same as their neighbor. This creates groups
    # of the same color/shape.
    for i in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


