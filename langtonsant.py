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


def main():
    bext.fg(ANT_COLOR) # The ants' color is the foreground color.
    bext.bg(WHITE_TITLE) # Set the background to white to start.
    bext.clear()

    # Create a new board data structure:
    board = {'width': WIDTH, 'height': HEIGHT}

    # Create ant data structures:
    ants = []
    for i in range(NUMBER_OF_ANTS):
        ant = {
            'x': random.randint(0, WIDTH - 1),
            'y': random.randint(0, HEIGHT - 1),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
        }
        ants.append(ant)
    
    # Keep track of which tiles have changed and need to be redrawn on
    # the screen:
    changedTiles = []
    
    while True: # Main program loop.
        displayBoard(board, ants, changedTiles)
        changedTiles = []
        
        # nextBoard is what the board will look like on the next step in
        # the simulation. Start with a copy of the current step's board:
        nextBoard = copy.copy(board)

        # Run a single simulation step for each ant:
        for ant in ants:
            if board.get((ant['x'], ant['y']), False) == True:
                nextBoard[(ant['x'], ant['y'])] = False
                # Turn clockwise:
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], any['y'])] = True
                # Turn counter clockwise:
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
            changedTiles.append((ant['x'], any['y']))

            # Move the ant forward in whatever direction it's facing:
            if ant['direction'] == NORTH:
                ant['y'] -= 1
            if ant['direction'] == SOUTH:
                ant['y'] += 1
            if ant['direction'] == WEST:
                ant['x'] -= 1
            if ant['direction'] == EAST:
                ant['x'] += 1

            # If the ant goes past the edge of the screen,
            # it should wrap around to the other side.
            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changedTiles.append((ant['x'], any['y']))

        board = nextBoard


