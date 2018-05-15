"""
29 April 2018.

Contains a greedy algorithm to solve Amstelhaege.  It generates a list with all
possible coordinates a house can have and iterates through this list for every
house to find the highest value place.  But, whenever a house gets placed, this
reduces the number of places the next house has.  The coordinates that are
impossible then get removed form the list.  Still needs a way to check if no house
is in another houses mandatory freespace.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import helpers.constraints as con
import classes.water as wt
import random
import numpy as np
import randomalgorithm as water
import helpers.coordinates as co

def greedy(plan):
    """ Performs a greedy algorithm.  Places the water randomly and places each
    house in an optimal place. houseNumber is the number of houses that have to
    be placed.  plan is the empty floorplan that will be filled.
    """

    plan.createCoordinates()

    plan.makePonds()

    # First house hasn't been placed yet
    firstHouse = False
    """
    while firstHouse == False:

        # Get random coordinates
        x = round(random.random() * plan.width, 1)
        y = round(random.random() * plan.length, 1)

        # Create house
        house1 = hs.Maison(x, y)

        distance = fch.findClosestHouse(plan.houses, house1)

        # Check if coordinates don't cross boundaries
        if distance > house1.freeSpace:

            # Save house with these coordinates
            plan.houses.append(house1)
            firstHouse = True
    """
    # Places the houses with a greedy algorithm
    for i in range(plan.numberOfHouses):

        # Decide what type of house will be placed. A testhouse is also made to
        # check for each coordinate if it's better than the current one. If it is,
        # the better coordinate will be saved

        bestX, bestY = 0, 0

        house = plan.makeHouse(bestX, bestY)

        bestX, bestY, distance = co.findCoordinates(plan, house)

        if distance < house.freeSpace:
            print("Error, no solution.")

        house.coordinates(bestX, bestY)
        print("distance: ", distance)

        if distance > 0:
            plan.houses.append(house)
        print("house ", len(plan.houses))

        co.removeCoordinates(plan, house)

    return plan

if __name__ == "__main__":
    plan = greedy(60)

    # Make visualisation
    plan.showFloorplan()
