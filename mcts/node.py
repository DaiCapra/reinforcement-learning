from abc import ABC, abstractmethod


class Node(ABC):
    def __init__(self):
        self.q = 0
        self.n = 0
        self.winner = 0
        self.current_player = 1

    def clear(self):
        self.q = 0
        self.n = 0
        self.winner = 0
        self.current_player = 1

    @abstractmethod
    def get_children(self):
        return set()

    @abstractmethod
    def is_terminal(self):
        return set()

    @abstractmethod
    def reward(self):
        return 0

    @abstractmethod
    def __hash__(self):
        return 0

    @abstractmethod
    def __eq__(self, other):
        return True
