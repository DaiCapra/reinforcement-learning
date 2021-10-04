from agents.monteAgent import MonteAgent
from agents.randomAgent import RandomAgent
from simulation import Simulation

# agents = [RandomAgent(), MonteAgent()]
# agents = [RandomAgent(), RandomAgent()]
agents = [MonteAgent(), MonteAgent()]
# agents = [MonteAgent(), RandomAgent()]

path = "weights.pkl"
number_of_games = 100

# load pre-trained weights
agents[0].load(path)
agents[1].load(path)

# simulate N games between agents
sim = Simulation()
result = sim.simulate(agents=agents, number_of_games=number_of_games, print_games=False)

d = {
    0: "draw",
    1: "agent 1",
    2: "agent 2"
}

print('number of games: ' + str(number_of_games))
for key in result:
    print(str(d[key]) + ': ' + str(result[key]))

