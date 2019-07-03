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

    print("\nPlayer 1: {}, Player 2: {}".format(player1_mark, player2_mark))

print("Welcome to Tic Tac Toe!\n")

# set player markers
player1_mark, player2_mark = player_input()

# create initial board
board = [' '] * 10

display_board(board)