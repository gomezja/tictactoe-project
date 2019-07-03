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

print("Welcome to Tic Tac Toe!\n")

player1_mark, player2_mark = player_input()
print("\nPlayer 1: {}, Player 2: {}".format(player1_mark, player2_mark))