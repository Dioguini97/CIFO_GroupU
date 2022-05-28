from random import uniform, choice
from operator import attrgetter


def fps(population):
    """Fitness proportionate selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """
    # Sum total fitness
    total_fitness = sum([i.fitness for i in population])
    # Get a 'position' on the wheel
    spin = uniform(0, total_fitness)

    if population.optim == "max":
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += individual.fitness
            if position > spin:
                return individual

    elif population.optim == "min":
        position = total_fitness
        # Find individual in the position of the spin
        for individual in population:
            position -= individual.fitness
            if position < spin:
                return individual

    else:
        raise Exception("No optimization specified (min or max).")


def tournament(population, size=2):
    """Tournament selection implementation.

    Args:
        population (Population): The population we want to select from.
        size (int): Size of the tournament.

    Returns:
        Individual: Best individual in the tournament.
    """

    # Select individuals based on tournament size
    tournament = [choice(population.individuals) for i in range(size)]
    # Check if the problem is max or min
    if population.optim == 'max':
        return max(tournament, key=attrgetter("fitness"))
    elif population.optim == 'min':
        return min(tournament, key=attrgetter("fitness"))
    else:
        raise Exception("No optimization specified (min or max).")




def ranking(population):
    """Linear ranking selection implementation.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """
    # Get the number of individuals in the population.
    n = population.size
    # Get a 'position' on the wheel
    spin = uniform(0, n)

    # # Use the gauss formula to get the sum of all ranks (sum of integers 1 to N).
    rank_sum = n * (n + 1) / 2

    # Sort and go through all individual fitnesses; enumerate ranks from 1.
    for rank, individual in enumerate(sorted(population), 1):
        yield rank, individual.fitness, rank / rank_sum

    if population.optim == "max":
        position = 0
        # Find individual in the position of the spin
        for individual in population:
            position += float(rank)
            if position > spin:
                return individual

    elif population.optim == "min":
        position = rank_sum
        # Find individual in the position of the spin
        for individual in population:
            position -= float(rank)
            if position < spin:
                return individual

    else:
        raise Exception("No optimization specified (min or max).")



