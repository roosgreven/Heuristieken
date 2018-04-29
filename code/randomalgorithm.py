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
import helpers.output as output

def RandomAlgorithm(houseNumber):

    # j checks how many times the while loop of house placement has run
    j = 0
    i = 0
    k = 0
    plan = FloorPlan(houseNumber)

    # Place four water ponds
    while k < 4:

        # Random coordinates
        x = round(random.random() * plan.width, 1)
        y = round(random.random() * plan.length, 1)

        # Initiate random water pond
        randomWaterPond = wt.Pond(x, y)

        if con.waterBoundary(plan, randomWaterPond):
            
            plan.ponds.append(randomWaterPond)
            k += 1

    # Loop over houses also check if while loop is not endless by using j
    while i < plan.numberOfHouses and j < 100000:

        # Get random coordinates.
        x = round(random.random() * plan.width, 1)
        y = round(random.random() * plan.length, 1)

        # Decide what type of house will be placed.
        if len(plan.houses) < plan.numberOfEengezins:
            randomHouse = hs.Eengezins(x, y)
            plan.currentEengezins += 1

        elif len(plan.houses) < plan.numberOfEengezins + plan.numberOfBungalows:
            randomHouse = hs.Bungalow(x, y)
            plan.currentBungalows += 1
        else:
            randomHouse = hs.Maison(x, y)
            plan.currentMaisons += 1

        # Add 1 to while loop counter
        j += 1

        # Check if there's overlap, if so, delete house from array and try again.
        if con.noOverlap(plan.houses, randomHouse, plan.ponds) and con.checkBoundaries(plan, randomHouse):
            
            # Add placed randomly house.
            plan.houses.append(randomHouse)
            i += 1
            
    print("Number of times iterated through loop:")
    print(j)
    output.Output(plan)

if __name__ == "__main__":
    RandomAlgorithm(60)
