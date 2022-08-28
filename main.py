import random
import itertools

class TicTacToe:

    def __init__(self, empty_sign="-"):
        self.board = []
        self.empty_sign = empty_sign

#Block bellow is not my code
###############################################################
    def create_board(self):
        for row in range(3):
            row_temp = []
            for column in range(3):
                row_temp.append(self.empty_sign)
            self.board.append(row_temp)

    def get_random_first_player(self):
        return random.randint(0,1)
################################################################

    def set_spot_value(self, row, column, player):
        if self.board[row][column] == self.empty_sign:
            self.board[row][column] = player
        else:
            # todo Hráč by měl dostat nový pokus.

    def does_anyone_win(self):

        game_over = None
        size_of_board = len(self.board)

        # Check rows
        for row in range(size_of_board):
            for column in range(size_of_board-2):
                if (self.board[row][column] == self.board[row][column+1]) and \
                   (self.board[row][column] == self.board[row][column+2]) and \
                   (self.board[row][column] != self.empty_sign):
                    game_over = True
            if game_over is True:
                return game_over

        # Check columns
        for column in range(size_of_board):
            for row in range(size_of_board - 2):
                if (self.board[row][column] == self.board[row + 1][column]) and \
                   (self.board[row][column] == self.board[row + 2][column]) and \
                   (self.board[row][column] != self.empty_sign):
                    game_over = True
            if game_over is True:
                return game_over

        # Check diagonals
        ## From left side
        for row in range(size_of_board - 2):
            for column in range(size_of_board - 2):
                if (self.board[row][column] == self.board[row + 1][column + 1]) and \
                   (self.board[row][column] == self.board[row + 2][column + 2]) and \
                   (self.board[row][column] != self.empty_sign):
                    game_over = True
            if game_over is True:
                return game_over

        ## From right side
        for row in range(size_of_board, 2, -1):
            for column in range(size_of_board, 2, -1):
                if (self.board[row][column] == self.board[row - 1][column - 1]) and \
                   (self.board[row][column] == self.board[row - 2][column - 2]) and \
                   (self.board[row][column] != self.empty_sign):
                    game_over = True
            if game_over is True:
                return game_over

    def is_board_full(self):
        if not any(field == self.empty_sign for field in list(itertools.chain.from_iterable(self.board))):
            return True



if __name__ == '__main__':
    game = TicTacToe
    game.does_anyone_win()