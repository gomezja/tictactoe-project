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
:param player1_mark: The marker for player one.
:param player2_mark: The marker for player two.
"""
def display_board(board, player1_mark, player2_mark):
    clear_output()

    print("   Tic Tac Toe\n")
    print("     |     |     ")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  ")
    print("     |     |     ")
    print("\nPlayer 1 = " + str(player1_mark))
    print("Player 2 = " + str(player2_mark) + "\n")

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
        try:
            position = int(input(str(turn) + " enter your move (1-9): "))
        except ValueError:
            pass

    return position

"""
Checks if board position is available.

:param board: A list of the current board.
:param position: The player's target space.
:returns: A boolean indicating space availability.
"""
def space_check(board, position):
    return board[position] == " "

"""
Checks if the board is completely full.

:param board: A list of the current board.
:returns: A boolean indicating if board is full.
"""
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

"""
Asks a question based on string parameter.

:param text: The string for the question being asked.
:returns: A boolean indicating the answer to the question.
"""
def check_play(text):
    choice = ''

    while not(choice == 'Y' or choice == 'N'):
        choice = input(str(text) + " (Y/N)? ").upper()

    return choice == 'Y'

#========================================

print("Welcome to Tic Tac Toe!\n")

while True:
    # set player markers
    player1_mark, player2_mark = player_input()

    # create initial board
    board = [' '] * 10

    # choose player that is going first
    print("\nChoosing player to go first...")
    turn = choose_first()
    print(str(turn) + " will go first.\n")

    # check if players are ready
    while not check_play("Ready to play"):
        if check_play("Exit game"):
            raise SystemExit(0)

    # active game
    while True:
        if turn == "Player 1":
            display_board(board, player1_mark, player2_mark)
            place_marker(board, player1_mark, player_choice(board, turn))

            if full_board_check(board):
                display_board(board, player1_mark, player2_mark)

                print("The game is a draw!")
                break
            else:
                turn = "Player 2"
        else:
            display_board(board, player1_mark, player2_mark)
            place_marker(board, player2_mark, player_choice(board, turn))

            if full_board_check(board):
                display_board(board, player1_mark, player2_mark)

                print("The game is a draw!")
                break
            else:
                turn = "Player 1"

    if not check_play("\nPlay again"):
        raise SystemExit(0)

    clear_output()