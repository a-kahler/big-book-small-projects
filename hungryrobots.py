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


def main():
    print('''Hungry Robots, by Austii KAY
    
You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly toward you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a personal teleporter device, but it only
has enough battery for {} trips. Keep in mind, you and robots can slip
through the corners of two diagonal walls!
'''.format(NUM_TELEPORTS))

    input('Press Enter to begin...')

    # Set up a new game:
    board = getNewBoard()
    robots = addRobots(board)
    playerPosition = getRandomEmptySpace(board, robots)
    while True: # Main game loop.
        displayBoard(board, robots, playerPosition)

        if len(robots) == 0: # Check if the player has won.
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # Move the player and robots:
        playerPosition = askForPlayerMove(board, robots, playerPosition)
        robots = moveRobots(board, robots, playerPosition)

        for x, y in robots: # Check if the player has lost.
            if (x, y) == playerPosition:
                displayBoard(board, robots, playerPosition)
                print('You have been caught by a robot!')
                sys.exit()


def getNewBoard():
    """Returns a dictionary that represents the board. The keys are
    (x, y) tuples of integer indexes for board positions, the values are
    WALL, EMPTY_SPACE, or DEAD_ROBOT. The dictionary also has the key
    'teleports' for the number of teleports the player has left.
    The living robots are stored separately from the board dictionary."""
    board = {'teleports': NUM_TELEPORTS}

    # Create an empty board:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE
    
    # Add walls on the edge of the board:
    for x in range(WIDTH):
        board[(x, 0)] = WALL # Make top wall.
        board[(x, HEIGHT - 1)] = WALL # Make bottom wall.
    for y in range(HEIGHT):
        board[(0, y)] = WALL # Make left wall.
        board[(WIDTH - 1, y)] = WALL # Make right wall.
    
    # Add the random walls:
    for i in range(NUM_WALLS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = WALL

    # Add the starting dead robots:
    for i in range(NUM_DEAD_ROBOTS):
        x, y = getRandomEmptySpace(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def getRandomEmptySpace(board, robots):
    """Return a (x, y) integer tuple of an empty space on the board."""
    while True:
        randomX = random.randint(1, WIDTH - 2)
        randomY = random.randint(1, HEIGHT - 2)
        if isEmpty(randomX, randomY, board, robots):
            break
    return (randomX, randomY)


def isEmpty(x, y, board, robots):
    """Return True if the (x, y) is empty on the board and there's also
    no robot there."""
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def addRobots(board):
    """Add NUM_ROBOTS number of robots to empty spaces on the board and 
    return a list of these (x, y) spaces where robots are now located."""
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = getRandomEmptySpace(board, robots)
        robots.append((x, y))
    return robots


