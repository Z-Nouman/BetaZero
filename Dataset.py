import numpy as np


class Dataset:

    def __init__(self):
        self.board = np.zeros((6, 7))
        self.turn = 1
        self.end = False
        self.victor = 0
        self.moves = 0

    """Resets the board with zeros"""

    def reset(self):
        # Bounds are between rows 0 - 5 and columns 0 - 6
        self.board = np.zeros((6, 7))
        self.victor = 0
        self.end = False
        self.turn = 1
        self.moves = 0

    def check_vertical_victory(self, state):
        for column in np.transpose(state):
            for j in range(3):
                if column[j] == column[j + 1] == column[j + 2] == column[j + 3] != 0:
                    self.end = True
                    self.victor = column[j]
                    return True
            # for token in column:
            #     if token == 0:
            #         continue
            #     vertical_sum += token
            #     if vertical_sum == 4 or vertical_sum == -4:
            #         self.end = True
            #         self.victor = vertical_sum / 4
            #         return True
        return False

    def check_horizontal_victory(self, state):
        for row in state:
            for j in range(4):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] != 0:
                    self.end = True
                    self.victor = row[j]
                    return True
        return False

    def check_diagonal_victory_down_right(self, state):
        for i in range(6):
            row = state.diagonal(-2 + i)
            for j in range(len(row) - 3):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] != 0:
                    self.end = True
                    self.victor = row[j]
                    return True
        return False

    def check_diagonal_victory_up_left(self, state):
        for i in range(6):
            row = np.flipud(state).diagonal(-2 + i)
            for j in range(len(row) - 3):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] != 0:
                    self.end = True
                    self.victor = row[j]
                    return True
        return False

    def get_state(self):
        return self.board, self.turn, self.end, self.victor

    def get_actions(self, state):
        return np.logical_not(state.all(0)).nonzero()

    def step(self, position):
        column = np.flatnonzero(self.board[:, position])

        if len(column) == 6:
            print("Error, can't make a move here!")
            print("Not making this move...")
            return

        if len(column) == 0:
            row = 5
        else:
            row = column[0] - 1

        self.board[row, position] = self.turn
        self.turn *= -1
        self.moves += 1
        return self.check_vertical_victory(self.board) or self. \
            check_horizontal_victory(self.board) or self. \
            check_diagonal_victory_down_right(self.board) or self. \
            check_diagonal_victory_up_left(self.board)

    def check_victory(self, state):
        return self.check_vertical_victory(state) or self. \
            check_horizontal_victory(state) or self. \
            check_diagonal_victory_down_right(state) or self. \
            check_diagonal_victory_up_left(state)

    def peek(self, position, state, player_num):
        column = np.flatnonzero(state[:, position])
        if len(column) == 6:
            print("Error, can't make a move here!")
            print("Not making this move...")
            return

        if len(column) == 0:
            row = 5
        else:
            row = column[0] - 1

        state[row, position] = player_num
        return state

    def display(self):
        print("\n")
        for i in self.board:
            for j in i:
                print("|", end=" ")
                if j == 1:
                    print(" X ", end=" ")
                elif j == -1:
                    print(" O ", end=" ")
                else:
                    print("   ", end=" ")
            print("|")
            print("-------------------------------------------")
        print("   0     1     2     3     4     5     6")
        print("\n")

