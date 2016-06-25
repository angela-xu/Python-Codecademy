'''
This is a simplified, one-player version of the classic board game Battleship.
In this version of the game, there will be a single ship hidden in a random location
on a 5*5 grid. The player will have 4 guesses to try to sink the ship.
'''

from random import randint
board = []

for x in range(5):
    board.append(['O'] * 5)

def print_board(board):
    for row in board:
        print(' '.join(row))

print('Let\'s play Battleship!')
print('There is a ship hidden in this 5 * 5 ocean.')
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# print(ship_row) for debugging only
# print(ship_col) for debugging only

for turn in range(4):
    print('Turn ' + str( turn + 1))
    guess_row = int(raw_input('Guess Row:'))
    guess_col = int(raw_input('Guess Col:'))

    if (guess_row - 1) == ship_row and (guess_col - 1) == ship_col:
        print('Congratulations! You sunk my battleship')
        board[guess_row - 1][guess_col - 1] = 'X'
        print_board(board)
        break
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print('Oops, that\'s not even in the ocean.')
        elif (board[guess_row - 1][guess_col - 1] == 'X'):
            print('You guessed that one already.')
        else:
            print('You missed my battleship!')
            board[guess_row - 1][guess_col - 1] = 'X'
        if turn == 3:
            print('Game Over.')

    print_board(board)
