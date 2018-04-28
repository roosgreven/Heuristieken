"""
24 April 2018.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.shortestdistance as sd
import helpers.findclosesthouse as fch
import random
import matplotlib.pyplot as plt
import helpers.constraints as con
import classes.water as wt

def RandomAlgorithm(houseNumber):

    i = 0
    plan = FloorPlan(houseNumber)
    totalValue = 0
    totalHouseValues = []

    # Place four water ponds
    while i < 4:

        # Random coordinates
        x = round(random.random() * plan.width, 1)
        y = round(random.random() * plan.length, 1)

        # Initiate random water pond
        randomWaterPond = wt(x, y, 20, 72)

        # Append to ponds array
        water.ponds.append(randomWaterPond)

    # Loop over houses.
    while i < plan.numberOfHouses:

        # Get random coordinates.
        x = round(random.random() * plan.width, 1)
        y = round(random.random() * plan.length, 1)

        if len(plan.houses) < plan.numberOfEengezins:
            randomHouse = hs.Eengezins(x, y)
            plan.currentEengezins += 1

        elif len(plan.houses) < plan.numberOfEengezins + plan.numberOfBungalows:
            randomHouse = hs.Bungalow(x, y)
            plan.currentBungalows += 1
        else:
            randomHouse = hs.Maison(x, y)
            plan.currentMaisons += 1

        # Check if there's overlap, if so, delete house from array and try again.
        if con.noOverlap(plan.houses, randomHouse) and con.checkBoundaries(plan, randomHouse):

            # Add placed randomly house.
            plan.houses.append(randomHouse)
            i += 1

    for house in plan.houses:

        distance = fch.findClosestHouse(plan.houses, house)
        totalValue += house.value(distance)

    print(totalValue)

    # Visualisation of the floor plan.
    plt.figure()

    for house in plan.houses:

        # By plotting these lists, all corners will be connected by a line.
        xlist = [house.x1, house.x2, house.x2, house.x1, house.x1]
        ylist = [house.y1, house.y1, house.y2, house.y2, house.y1]

        plt.plot(xlist, ylist)

    plt.show()


if __name__ == "__main__":
    RandomAlgorithm(60)
