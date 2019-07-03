import random

"""
Player 1 chooses their marker.

:returns: A tuple with player 1 and player 2 markers.
"""
def player_input():
    choice = ''

    while not(choice == 'X' or choice == 'O'):
        choice = input("Player 1: please pick a marker 'X' or 'O': ").upper()
    
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

"""
    Function uses random int (0 or 1) to decide which player goes first.

    :returns: Player who goes first.
"""
def choose_first():
    if random.randint(0,1):
        return "Player 1"
    else:
        return "Player 2"

"""
Clears screen between board updates.
"""
def clear_output():
    print("\n" * 100)

"""
Displays the current game board.

:param board: A list with all the current markers on the board.
"""
def display_board(board):
    clear_output()

    print("    |   |    ")
    print("  " + board[7] + " | " + board[8] + " | " + board[9] + "  ")
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print("  " + board[4] + " | " + board[5] + " | " + board[6] + "  ")
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print("  " + board[1] + " | " + board[2] + " | " + board[3] + "  ")
    print("    |   |    ")

"""
Updates the board list with the new marker.

:param board: A list of the current board.
:param marker: The marker being placed.
:param position: The position being updated.
"""
def place_marker(board, marker, position):
    board[position] = marker

"""
The function validates a players chosen move.

:param board: A list of the current game board.
:param turn: The current player choosing move.
:returns: A valid player move.
"""
def player_choice(board, turn):
    position = 0

    while position not in range(1,10) or not space_check(board, position):
        position = int(input(str(turn) + " enter your move: "))

    return position

"""
Checks if board position is available.

:returns: A boolean indicating space availability.
"""
def space_check(board, position):
    return board[position] == " "

print("Welcome to Tic Tac Toe!\n")

# set player markers
player1_mark, player2_mark = player_input()

# create initial board
board = [' '] * 10

turn = choose_first()

game_on = True
display_board(board)

while game_on:
    if turn == "Player 1":
        place_marker(board, player1_mark, player_choice(board, turn))
        display_board(board)

        turn = "Player 2"
    else:
        place_marker(board, player2_mark, player_choice(board, turn))
        display_board(board)

        turn = "Player 1"