import random

from agents.agent import Agent
from mcts.node import Node


class RandomAgent(Agent):
    def get_action(self, state: Node):
        children: dict = state.get_children()
        choice = random.choice(children)
        return choice
