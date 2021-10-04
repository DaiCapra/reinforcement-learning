from tqdm import tqdm

from agents.agent import Agent
from mcts.node import Node
from mcts.tree_search import TreeSearch
from training import save, load


class MonteAgent(Agent):
    iterations = 100

    def __init__(self, iterations: int = 100) -> None:
        super().__init__()
        self.ts = TreeSearch()
        self.iterations = iterations

    def train(self, state: Node, count, verbose=False):
        if verbose:
            for i in tqdm(range(count)):
                self.ts.rollout(state)
        else:
            for i in range(count):
                self.ts.rollout(state)

    def get_action(self, state: Node):
        self.train(state, self.iterations)
        best = self.ts.choose(state)
        return best

    def save(self, path):
        save(path, self.ts.nodes)

    def load(self, path):
        nodes = load(path)
        self.ts.nodes = nodes
