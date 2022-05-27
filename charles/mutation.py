from random import choice, randint, sample


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
