import random
import seaborn as sns
import numpy as np
from operator import add 

def roller(
    dice_roles: int,
    sides_of_dice: int,
    simulations: int,
    modifier: int,
    advantage: bool = False,
    disadvantage: bool = False
) -> list:
    """
    Columns are number of unique rolls.
    Rows are number of role simulations and a possible modifier that way sums across rows can be performed.
    """
    # build sim rand roles
    
        
    if advantage:
        roles_1 = []
        for role in range(dice_roles):
            roles_1.append([random.randint(1, sides_of_dice) for iter in range(simulations)])
        
        roles_2 = []
        for role in range(dice_roles):
            roles_2.append([random.randint(1, sides_of_dice) for iter in range(simulations)])
        
        roles_1 = np.array(roles_1)
        roles_2 = np.array(roles_2)

        roles = np.maximum(roles_1, roles_2).tolist()
    elif disadvantage:
        roles_1 = []
        for role in range(dice_roles):
            roles_1.append([random.randint(1, sides_of_dice) for iter in range(simulations)])
        
        roles_2 = []
        for role in range(dice_roles):
            roles_2.append([random.randint(1, sides_of_dice) for iter in range(simulations)])
            
        roles_1 = np.array(roles_1)
        roles_2 = np.array(roles_2)
        
        roles = np.minimum(roles_1, roles_2).tolist()
    else:
        roles = []
        for role in range(dice_roles):
            roles.append([random.randint(1, sides_of_dice) for iter in range(simulations)])

    # mod
    mods = [modifier] * simulations
    add_mod = [[xi + y for xi in x] for x, y in zip(roles, mods)]
    role_sims = [sum(i) for i in zip(*add_mod)]

    return role_sims