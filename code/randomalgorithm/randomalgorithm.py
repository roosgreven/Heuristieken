"""
24 April 2018.

Performs a random algorithm to solve Amstelhaege.  First places all the water
randomly, then places all houses randomly. It always checks if a water or house
is actually allowed to be placed at a certain coordinate befor placing it.  Still
needs a way to check if all houses were actually placed in the given number of
iteratations and if not handle accordingly.
"""

from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import random
import matplotlib.pyplot as plt
import helpers.constraints as con
import classes.water as wt

def randomAlgorithm(plan):
    """ Performs a random algorithm, first placing water, then placing houses.
    houseNumber is the number of houses that have to be in the neighbourhood.
    plan is the empty floorplan that will be filled.
    """

    # j checks how many times the while loop of house placement has run
    j = 0
    i = 0

    plan.makePonds()

    # Loop over houses also check if while loop is not endless by using j
    while i < plan.numberOfHouses and j < 100000:

        # Get random coordinates
        x, y = plan.randomCoordinates()

        randomHouse = plan.makeHouse(x, y)

        # Add 1 to while loop counter
        j += 1

        # Check if there's overlap, if not, add house to array
        if con.noWaterAndBoundary(randomHouse, plan):

            distance = fch.findClosestHouse(plan, randomHouse)

            if not distance < randomHouse.freeSpace:
                # Add randomly placed house
                plan.houses.append(randomHouse)
                i += 1

    print("Number of times iterated through loop:")
    print(j)

    return plan



if __name__ == "__main__":
    plan = randomAlgorithm(60)

    # Make visualisation
    plan.showFloorplan()
