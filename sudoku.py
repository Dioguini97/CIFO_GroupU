from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from copy import deepcopy
from data.sudoku_data import values
from charles.selection import fps, tournament
from charles.mutation import replace_mutation
from charles.crossover import single_point_co
from random import random
from operator import attrgetter


def get_fitness(self):
    """A fitness function for the Sudoku Problem.
    Calculates the fitness of rows, columns and blocks in terms of repetition and sum

    Returns:
        int: the closer to 0 the better
    """

    rows = 0
    columns = 0
    blocks = 0

    for i in range(9):
        sum = 0
        for j in range(9):
            sum = sum + self.representation[i * 9 + j]
        rows = rows + abs(sum - 45)

    for i in range(9):
        sum = 0
        for j in range(9):
            sum = sum + self.representation[i + j * 9]
        columns = columns + abs(sum - 45)

    for box_num in range(9):
        row = 3 * int(box_num / 3)
        col = 3 * (box_num % 3)
        sum = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                sum = sum + self.representation[i * 9 + j]
        blocks = blocks + abs(sum - 45)

    return rows + columns + blocks


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
    size=20, optim="min", init_repr=values, valid_set=[1, 2, 3, 4, 5, 6, 7, 8, 9]
)

pop.evolve(gens=100,
           select=tournament,
           crossover=single_point_co,
           mutate=replace_mutation,
           co_p=0.9, mu_p=0.1,
           elitism=True)
