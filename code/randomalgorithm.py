"""
24 April 2018.

Random algorithm.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import random
import matplotlib.pyplot as plt
import helpers.constraints as con
import classes.water as wt

def randomAlgorithm(houseNumber):

    # j checks how many times the while loop of house placement has run
    j = 0
    i = 0
    plan = FloorPlan(houseNumber)

    # Place four water ponds
    while len(plan.ponds) < 4:

        # Get random coordinates
        x, y = random_coordinates(plan)

        # Call water placement function
        water_placement(x, y, plan)

    # Loop over houses also check if while loop is not endless by using j
    while i < plan.numberOfHouses and j < 100000:

        # Get random coordinates
        x, y = random_coordinates(plan)

        randomHouse = house_placement(x, y, plan)

        # Add 1 to while loop counter
        j += 1

        # Check if there's overlap, if not, add house to array
        if con.noOverlap(plan.houses, randomHouse, plan.ponds) and con.checkBoundaries(plan, randomHouse):

            # Add placed randomly house
            plan.houses.append(randomHouse)
            i += 1

    print("Number of times iterated through loop:")
    print(j)

    return plan

""" Places water at random location """
def water_placement(x, y, plan):

    # Initiate random water pond
    WaterPond = wt.Pond(x, y)

    if con.waterCheck(plan, WaterPond):

        plan.ponds.append(WaterPond)

""" Sets random coordinates x and y. """
def random_coordinates(plan):

    # Random coordinates
    x = round(random.random() * plan.width, 1)
    y = round(random.random() * plan.length, 1)
    return x, y

""" Initiates new house to place """
def house_placement(x, y, plan):
    # Decide what type of house will be placed
    if len(plan.houses) < plan.numberOfEengezins:
        house = hs.Eengezins(x, y)

    elif len(plan.houses) < plan.numberOfEengezins + plan.numberOfBungalows:
        house = hs.Bungalow(x, y)

    else:
        house = hs.Maison(x, y)

    return house

if __name__ == "__main__":
    RandomAlgorithm(60)
