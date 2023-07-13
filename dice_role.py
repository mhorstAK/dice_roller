import random
import seaborn as sns
import numpy as np

def roller(
    dice_roles: int,
    sides_of_dice: int,
    simulations: int,
    modifier: int
) -> list:
    """
    Columns are number of unique rolls.
    Rows are number of role simulations and a possible modifier that way sums across rows can be performed.
    """
    # build sim rand roles
    roles = []
    for role in range(dice_roles):
        roles.append([random.randint(1, sides_of_dice) for iter in range(simulations-1)])

    # mod
    mods = [modifier] * simulations
    add_mod = [[xi + y for xi in x] for x, y in zip(roles, mods)]
    role_sims = [sum(i) for i in zip(*add_mod)]

    return role_sims