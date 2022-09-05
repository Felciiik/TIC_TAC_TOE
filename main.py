import random
import textwrap
import itertools

class TicTacToe:

    def __init__(self, empty_sign="-"):
        self.board = []
        self.empty_sign = empty_sign
        self.board_size = self.choose_size_of_board()

    def choose_size_of_board(self):
        while True:
            size = input(textwrap.dedent("""
                                    --- \n
                                    Choose size of game board (Enter number). \n
                                    (Minimal size of board is 3 and maximal size of board is 10) \n
                                    (size of board will be entered number x entered number e.g. 3x3) \n
                                    --- \n
                                        """))
            try:
                size = int(size)
            except:
                print(textwrap.dedent("""
                                --- \n
                                You entered wrong symbol. \n
                                Enter only number. \n
                                --- \n
                                     """))
                continue

            if 3 <= size <= 10:
                break
            else:
                print(textwrap.dedent("""
                                --- \n
                                Minimal size of board is 3 and maximal size of board is 10. \n
                                Enter only number. \n
                                --- \n
                                     """))
                continue
        return size


#Block bellow is not my code
###############################################################

    def create_board(self):
        for row in range(self.board_size):
            row_temp = []
            for column in range(self.board_size):
                row_temp.append(self.empty_sign)
            self.board.append(row_temp)

################################################################

    def first_player_choose_sign(self):
        while True:
            player = input(textwrap.dedent("""
                                    --- \n
                                    First player enter your sign ('X' or 'O'). \n
                                    --- \n
                                          """))
            if player == "X" or "O":
                break
            else:
                continue
        return player

    def choose_field_with_check(self, player):
        while True:
            player_row_col = input(textwrap.dedent("""
                                --- \n
                                Enter row, column numbers to occupy chosen field. \n
                                Required format is row and column number separated by comma.  \n
                                For example '2, 3'. \n
                                --- \n
                                                    """))
            player_row_col = player_row_col.replace(" ", "").split(",")
            if len(player_row_col) != 2:
                print(textwrap.dedent("""
                                --- \n
                                You entered row and column in wrong format. \n
                                There was probably too many commas (",") \n
                                Read guidelines again and enter row adn column again. \n
                                --- \n
                                      """))
                continue
            try:
                row, col = list(map(int, (player_row_col)))
            except ValueError:
                print(textwrap.dedent("""
                                --- \n
                                You entered row and column in wrong format. \n
                                At least one symbol around comma is not number or there are some unwanted symbols.\n
                                Read guidelines again and enter row adn column again. \n
                                --- \n
                                    """))
                continue
            if row < 1 or col < 1:
                print(textwrap.dedent("""
                                --- \n
                                You entered row and column in wrong format. \n
                                At least one number is lower than 1 (There can not be negative rows\cols). \n
                                Read guidelines again and enter row adn column again. \n
                                --- \n
                                      """))
                continue
            row, col = row - 1, col - 1  # Zeroindexing

            if self.board[row][col] == self.empty_sign:
                self.set_spot_value(row, col, player)
                break
            else:
                print(textwrap.dedent("""
                                    --- \n
                                    You entered coordinates of occupied field. \n
                                    Try it again. \n
                                    --- \n
                                      """))
                continue


    def set_spot_value(self, row, column, player):
            self.board[row][column] = player

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

        def helper_function(size_of_board):
            if size_of_board == 3:
                iterator = [2]
            else:
                iterator = range(size_of_board-1, 2, -1)
            return iterator

        ## From right side
        for row in helper_function(size_of_board):
            for column in helper_function(size_of_board):
                if (self.board[row][column] == self.board[row - 1][column - 1]) and \
                   (self.board[row][column] == self.board[row - 2][column - 2]) and \
                   (self.board[row][column] != self.empty_sign):
                    game_over = True
            if game_over is True:
                return game_over

    def is_board_full(self):
        if not any(field == self.empty_sign for field in list(itertools.chain.from_iterable(self.board))):
            return True

    def swap_player(self, player):
        return "X" if  player == "O" else "O"

    def show_board(self):
        print("-----" * len(self.board))
        for row in self.board:
            for column in row:
                print("| " + column + " |", end="")
            print("\n", end="")
            print("-----" * len(row))

    def start_game(self):

        size = self.board_size

        self.create_board()

        player = self.first_player_choose_sign()

        while True:
            print(f'Turn of player {player}: \n')

            self.show_board()

            self.choose_field_with_check(player)

            if self.does_anyone_win():
                print(f"Player {player} wins the game!")
                break
                #todo Nabídni, zda chce hráč skončit nebo začít novou hru.

            if self.is_board_full():
                print("It's draw. All fields are occupied.")

            player = self.swap_player(player)

        self.show_board()



if __name__ == '__main__':
    game = TicTacToe()
    game.start_game()