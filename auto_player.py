import random

board_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board =[" "," "," ",
        " "," "," ",
        " "," "," ",]

class autoPlayer:
    def __init__(self, board, board_positions):
        self.board = board
        self.board_positions = board_positions
    # position = int(input("1-9: "))

    def auto_moves(self, position):
        self.position = position
        # remove the layers first move from the board positions list
        self.board_positions.remove(self.position)

        if "O" not in self.board:
            # logic for FIRST MOVE
            # if opponent takes centre, take a corner
            # if opponent takes a corner, take the centre or a corner
            best_pos = [1,3,5,7,9]
            if self.position in best_pos:
                best_pos.remove(self.position)

            move = random.choice(best_pos)
            self.board_positions.remove(move)

            move = int(move) - 1
            self.board[move] = "O"
            return None

    def check_row_possible_wins(self):
        row_1 = self.board[0:3]
        row_2 = self.board[3:6]
        row_3 = self.board[6:9]
        if row_1.count("O") == 2 and row_1.count(" ") == 1:
            # move should be in the possition that is empty
            return self.board_positions[0]
        elif row_2.count("O") == 2 and row_2.count(" ") == 1:
            # move should be in the possition that is empty
            for i in range(0, len(self.board_positions)):
                if self.board_positions[i] > 2 and self.board_positions[i] < 6:
                    return self.board_positions[i]
        elif row_2.count("O") == 2 and row_2.count(" ") == 1:
            # move should be in the possition that is empty
            return self.board_positions[-1]
        return

'''
LOGIC:
check that it is the auto turn
if it is, is it the first move?
first move best position on the quincunx

for successive moves:
- check if auto has 2 in a direction with a free space (to win)
if auto does:
- go there and win

otherwise:
- check if the other player has 2 in any direction
if they do:
- block

if they do not:
- go in a space where there are 2 empty spaces in that direction
(go somewhere where it is still possible to make 3 in a row)

if not possible to create a 3 in any direction:
- go in any remaining space
'''

