import math
from copy import copy

import numpy as np

from mcts.node import Node


class Board(Node):
    pieces = {
        0: "-",
        1: "x",
        2: "o",
    }
    width = 3
    height = 3

    def __init__(self):
        super().__init__()
        self.size = self.width * self.height
        self.board = np.zeros(self.size, dtype=int)

    def clear(self):
        super().clear()
        self.board.fill(0)

    def copy(self):
        state = Board()
        state.board = copy(self.board)
        state.current_player = self.current_player
        return state

    def get_children(self):
        children = []

        a = self.board
        indices = np.where(a == 0)

        for index in indices[0]:
            state: Board = self.copy()
            state.make_move_by_index(index)
            children.append((state, index))

        return children

    def increment_player(self):
        self.current_player += 1
        if self.current_player >= 3:
            self.current_player = 1

    def is_terminal(self):
        if self.winner > 0:
            return True

        if len(self.get_children()) <= 0:
            return True

        return False

    def reward(self):
        return self.winner

    def make_move(self, x, y):
        index = self.get_index_by_position(x, y)
        self.make_move_by_index(index)

    def make_move_by_index(self, index):
        self.board[index] = self.current_player
        self.increment_player()
        self.winner = self.check_winner()

    def set_value(self, x, y, value):
        index = self.get_index_by_position(x, y)
        self.board[index] = value

    def get_position_by_index(self, index):
        y = math.floor(index / self.height)
        x = index % self.height
        return x, y

    def get_index_by_position(self, x, y):
        index = y * self.height + x
        return index

    def check_winner(self):
        b = self.reshape_to_matrix(self.board)
        for i in range(2):
            player = i + 1
            mask = b == player
            out = mask.all(0).any() | mask.all(1).any()
            out |= np.diag(mask).all() | np.diag(mask[:, ::-1]).all()

            if out:
                return player

        return 0

    def print(self):
        m = self.reshape_to_matrix(self.board)
        board = "\n"
        for row in m:
            s = np.array_str(row)
            for key in self.pieces:
                value = self.pieces[key]
                s = s.replace(str(key), value)

            board += s
            board += "\n"

        print(board)

    def reshape_to_matrix(self, array):
        return np.reshape(array, (self.width, -1))

    def __hash__(self):
        b = self.board.tobytes()
        h = hash(b)
        return h

    def __eq__(self, other):
        o: Board = other
        return o.__hash__() == self.__hash__()

    def __str__(self) -> str:
        return f"{self.board} {self.current_player}".replace("\n", " ")
