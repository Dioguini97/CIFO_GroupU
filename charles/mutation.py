from random import choice, sample


def replace_mutation(individual, mutable_indexes, valid_set):
    """Replace mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get a mutation point
    mut_point = choice(mutable_indexes)
    # Mutate it
    individual[mut_point] = choice(valid_set)
    return individual


def swap_mutation(individual, mutable_indexes, valid_set):
    """Swap mutation for a GA individual

    Args:
        individual (Individual): A GA individual from charles.py

    Returns:
        Individual: Mutated Individual
    """
    # Get two mutation points
    mut_points = sample(mutable_indexes, 2)
    # Swap them
    individual[mut_points[0]], individual[mut_points[1]] = individual[mut_points[1]], individual[mut_points[0]]

    return individual
