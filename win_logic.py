board =[" "," "," ",
        " "," "," ",
        " "," "," ",]

class win_logic:

    def __init__(self, board):
        self.board = board


    def check_rows(self):
        row_1 = self.board[0] == self.board[1] == self.board[2] != " "
        row_2 = self.board[3] == self.board[4] == self.board[5] != " "
        row_3 = self.board[6] == self.board[7] == self.board[8] != " "

        # if row_1 or row_2 or row_3:
        #     return False

        if row_1:
            return self.board[0]
        elif row_2:
            return self.board[3]
        elif row_3:
            return self.board[6]
        return None

    def check_columns(self):
        column_1 = self.board[0] == self.board[3] == self.board[6] != " "
        column_2 = self.board[1] == self.board[4] == self.board[7] != " "
        column_3 = self.board[2] == self.board[5] == self.board[8] != " "

        # if column_1 or column_2 or column_3:
        #     return False

        if column_1:
            return self.board[0]
        elif column_2:
            return self.board[1]
        elif column_3:
            return self.board[2]
        return None

    def check_diagonals(self):
        diagonal_1 = self.board[0] == self.board[4] == self.board[8] != " "
        diagonal_2 = self.board[2] == self.board[4] == self.board[6] != " "

        # if diagonal_1 or diagonal_2:
        #     return False

        if diagonal_1:
            return self.board[0]
        elif diagonal_2:
            return self.board[2]
        return None

    def check_if_game_over(self):
        winner = self.check_if_win()
        tie = self.check_if_tie()
        return winner, tie

    def check_if_win(self):
        # check rows
        row_winner = self.check_rows()
        # check columns
        column_winner = self.check_columns()
        # check diagonals
        diagonal_winner = self.check_diagonals()
        if row_winner:
            winner = row_winner
        elif column_winner:
            winner = column_winner
        elif diagonal_winner:
            winner = diagonal_winner
        else:
            winner = None
        return winner

    def check_if_tie(self):
        if " " not in self.board:
            return True
        return None