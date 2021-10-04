import math
import random
from collections import defaultdict

from mcts.node import Node


class TreeSearch:
    def __init__(self, weight_exploration=math.sqrt(2)):
        self.weight_exploration = weight_exploration
        self.nodes = dict()
        self.expanded = defaultdict()
        self.has_no_valid_children = dict()

    def rollout(self, node: Node):
        # select node to explore
        path = self.select(node)

        # explored selected node
        last = path[-1]
        self.expand(last)

        # simulate reward for node
        reward = self.simulate(last)

        # backpropagate reward from selected node to root
        self.backpropagate(path, reward)

    def choose(self, node: Node):
        if not self.is_expanded(node):
            children: dict = node.get_children()
            choice = random.choice(children)
            return choice
        else:
            def score(t):
                child: Node = t[0]
                if child.n == 0:
                    return -math.inf
                s = child.q / child.n
                return s

            children = self.nodes[node]
            m = max(children, key=score)
            return m

    def backpropagate(self, path, reward):
        for p in reversed(path):
            node: Node = p
            node.q += reward
            node.n += 1
            reward = 1 - reward

    def expand(self, node: Node):
        # exit if node has been expanded
        if self.is_expanded(node):
            return

        self.expanded[node] = True

        # children = node.get_children()
        # self.nodes[node] = children

    def select(self, node: Node):
        path = []

        current: Node = node
        while True:
            # add current to pass
            path.append(current)

            if self.is_terminal(current) or not self.is_expanded(current):
                return path

            # try find a child that hasn't been expanded
            valid_child = None
            if current not in self.has_no_valid_children:
                for child in self.get_children(current):
                    state = child[0]
                    if not self.is_expanded(state):
                        valid_child = state
                        break

            if valid_child is None:
                self.has_no_valid_children[current] = True

                # traverse depth
                current = self.uct(current)
            else:
                current = valid_child

    def get_children(self, node: Node):
        if node in self.nodes:
            return self.nodes[node]

        c = node.get_children()
        self.nodes[node] = c
        return self.nodes[node]

    def get_child_tuples(self, node: Node):
        if node in self.nodes:
            return self.nodes[node]
        return []

    def is_expanded(self, node: Node):
        return node in self.expanded
        # return node in self.nodes

    def simulate(self, node: Node):
        player = node.current_player
        current: Node = node

        while True:
            if self.is_terminal(current):
                winner = current.reward()
                if winner == player:
                    return 0
                elif winner == 0:
                    return 0.5
                else:
                    return 1

            children = self.get_children(current)
            random_state = random.choice(children)

            current = random_state[0]

    def uct(self, node: Node):
        children = self.get_children(node)
        if node.n > 0:
            log_n = math.log(node.n)
        else:
            log_n = math.inf

        def utc_score(t):
            state: Node = t[0]
            if state.n == 0:
                return math.inf
            score = state.q / state.n + self.weight_exploration * math.sqrt(log_n / state.n)
            return score

        m = max(children, key=utc_score)
        return m[0]

    def is_terminal(self, node: Node):
        if node.winner > 0:
            return True

        children = self.get_children(node)

        if len(children) <= 0:
            return True

        return False
