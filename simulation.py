from tqdm import tqdm

from games.tictactoe.board import Board


class Simulation:
    def simulate(self, agents: list, number_of_games=1, print_games=False):
        game = Board()

        wins = {}
        for i in range(len(agents) + 1):
            wins[i] = 0

        for g in tqdm(range(number_of_games)):
            game.clear()
            while not game.is_terminal():
                for i in range(len(agents)):
                    agent = agents[i]
                    action = agent.get_action(game)
                    index = action[1]
                    game.make_move_by_index(index)

                    if (print_games):
                        game.print()

                    if game.is_terminal():
                        winner = game.winner
                        if winner > 0:
                            wins[winner] += 1
                        else:
                            wins[0] += 1
                        break

        return wins
