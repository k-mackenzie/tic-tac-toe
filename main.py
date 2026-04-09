import auto_player
import win_logic as win

""" GLOBAL VARIABLES """
game_still_going = True
winner = None
current_player = "X"

board =[" "," "," ",
        " "," "," ",
        " "," "," ",]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--|---|--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--|---|--")
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    global game_still_going
    # display the initial board
    display_board()

    while game_still_going:

        # handle turn of a single player
        handle_turn(current_player)

        # check if the game has ended
        win_check = win.win_logic(board)
        winner, tie = win_check.check_if_game_over()

        # game has ended:
        if winner: #== "X" or winner == "O":
            print(winner + " won!")
            game_still_going = False
        elif tie: #winner == None:
            print("Tie.")
            game_still_going = False

        # flip to the other player
        flip_player()


# handle the turn of a player
def handle_turn(player):
    print(player + "'s turn")
    # first get pos from player
    position = input("choose a position from 1-9: ")
    # position = int(position) - 1

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("INVALID INPUT: choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] != " ":
            position = input("position already taken! try a different one: ")
        else:
            valid = True


    # position = int(position) - 1
    board[position] = player
    display_board()



def flip_player():
    global current_player
    # flip player from X to O
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()



# display_board()

#

# board
# display
# play game (alternate players)
# handle a turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
    # board is full and no winner
# flip player