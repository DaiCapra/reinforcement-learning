from abc import ABC, abstractmethod
from mcts.node import Node


class Agent(ABC):
    @abstractmethod
    def get_action(self, state: Node):
        return None
