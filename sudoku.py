from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from copy import deepcopy
from data.sudoku_data import values
from charles.selection import fps, tournament
from charles.mutation import binary_mutation
from charles.crossover import single_point_co
from random import random
from operator import attrgetter


def get_fitness(self):
    """A fitness function for the Sudoku Problem.
    Calculates ...
    Otherwise, the fitness value will be proportional to how bad it is.

    Returns:
        int: ...
    """
    fitness = 0
    # weight = 0
    # for bit in range(len(self.representation)):
    #     if self.representation[bit] == 1:
    #         fitness += values[bit]
    #         weight += weights[bit]
    # if weight > capacity:
    #     fitness = capacity-weight
    return fitness


def get_neighbours(self):
    """A neighbourhood function for the Sudoku Problem.

    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation))]

    for count, i in enumerate(n):
        if i[count] == 1:
            i[count] = 0
        elif i[count] == 0:
            i[count] = 1

    n = [Individual(i) for i in n]
    return n


# Monkey Patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

pop = Population(
    size=20, optim="max", sol_size=len(values), valid_set=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], replacement=True
)

pop.evolve(gens=100,
           select=tournament,
           crossover=single_point_co,
           mutate=binary_mutation,
           co_p=0.9, mu_p=0.1,
           elitism=True)
