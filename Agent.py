from Dataset import Dataset
import numpy as np
from Model import Model
from math import inf


class Agent:

    def __init__(self, board: Dataset, model: Model, computer=True):
        self.board = board
        self.computer = computer
        self.model = model
        return

    def random_move(self):
        possible_actions = np.ravel(self.board.get_actions(self.board.get_state()[0]))
        if len(possible_actions) == 0:
            self.board.end = True
            return
        return self.board.step(np.random.choice(possible_actions))

    def action(self):
        if not self.computer:
            try:
                if self.board.end:
                    return
                column = int(input("Enter a number, 0 - 6, to place a token in that column: "))
                self.board.step(column)
            except:
                print("Invalid input, please try again with an integer 0 - 6!")
                raise
        else:
            if self.board.end:
                return
            possible_actions = np.ravel(self.board.get_actions(self.board.get_state()[0]))
            if len(possible_actions) == 0:
                self.board.end = True
                return

            peek = np.copy(self.board.get_state()[0])
            return self.board.step(self.minimax(peek, -inf, inf, 1, 7)[0])

    def minimax(self, board, a, b, player_num, depth):
        if depth == 0:
            return None, -1 * self.model.predict(board)
        actions = np.ravel(self.board.get_actions(board))
        winner = self.peek_victory(board)
        if winner != 0:
            if winner == -1:
                return None, 1000000
            else:
                return None, -inf
        decision = -1
        if player_num == -1:
            utility = -inf
            for action in actions:
                new_state = np.copy(self.board.peek(action, board, player_num))
                new_utility = self.minimax(new_state, a, b, player_num * -1, depth - 1)
                if new_utility[1] >= utility:
                    utility = new_utility[1]
                    decision = action
                if utility > a:
                    a = utility
                if a >= b:
                    break
            return decision, utility
        else:
            utility = inf
            for action in actions:
                new_state = np.copy(self.board.peek(action, board, player_num))
                new_utility = self.minimax(new_state, a, b, player_num * -1, depth - 1)
                if new_utility[1] <= utility:
                    utility = new_utility[1]
                    decision = action
                if utility < b:
                    b = utility
                if a >= b:
                    break
            return decision, utility

    def peek_vertical_victory(self, state):
        for column in np.transpose(state):
            for j in range(3):
                if column[j] == column[j + 1] == column[j + 2] == column[j + 3] != 0:
                    return column[j]
        return 0

    def peek_horizontal_victory(self, state):
        for row in state:
            for j in range(4):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] != 0:
                    return row[j]
        return 0

    def peek_diagonal_victory_down_right(self, state):
        for i in range(6):
            row = state.diagonal(-2 + i)
            for j in range(len(row) - 3):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] != 0:
                    return row[j]
        return 0

    def peek_diagonal_victory_up_left(self, state):
        for i in range(6):
            row = np.flipud(state).diagonal(-2 + i)
            for j in range(len(row) - 3):
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3] != 0:
                    return row[j]
        return 0

    def peek_victory(self, state):
        return self.peek_vertical_victory(state) + self.peek_horizontal_victory(
            state) + self.peek_diagonal_victory_down_right(state) + self.peek_diagonal_victory_up_left(state)
