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
import helpers.output as output
import random
import numpy as np
import randomalgorithm as water

def greedy(houseNumber):
    """ Performs a greedy algorithm.  Places the water randomly and places each
    house in an optimal place. houseNumber is the number of houses that have to
    be placed.
    """
    
    plan = FloorPlan(houseNumber)

    plan.createCoordinates()
    
    # Place four water ponds
    while len(plan.ponds) < 4:

        # Get random coordinates
        x, y = water.random_coordinates(plan)

        # Call water placement function
        water.water_placement(x, y, plan)

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
    for i in range(houseNumber):
        
        # Decide what type of house will be placed. A testhouse is also made to
        # check for each coordinate if it's better than the current one. If it is,
        # the better coordinate will be saved
        
        bestX, bestY = 0, 0
        
        if i < plan.numberOfMaisons:
            
            house = hs.Maison(0, 0)

        elif i < plan.numberOfMaisons + plan.numberOfBungalows:

            house = hs.Bungalow(0, 0)

        else:
            house = hs.Eengezins(0, 0)
            
        distance = 0

        # Looks for the best coordinate to place a house
        for coordinate in plan.coordinates:

            x, y = coordinate[0], coordinate[1]

            # The house is set to new coordinate
            house.coordinates(x, y)

            # Check if it can be placed there
            if con.noWaterAndBoundary(house, plan):

                # Find closest distance to house or border
                newDistance = fch.findClosestHouse(plan.houses, house)

                # If there's more freespace in this position, take over coordinates
                if newDistance > distance:

                    distance = newDistance
                    bestX, bestY = x, y
                    
        if distance < house.freeSpace:
            print("Error, no solution.")
                        
        house.coordinates(bestX, bestY)
        print("distance: ", distance)
        plan.houses.append(house)
        print("house ", len(plan.houses))

        # All coordinates that have guaranteed become unavailable because of the
        # house that was just placed, are removed from the list of coordinates
        for x in np.arange(house.x1 - house.freeSpace - plan.eengezinsWidth + 1, house.x2 + house.freeSpace, 0.5):
            for y in np.arange(house.y1 - house.freeSpace - plan.eengezinsLength + 1, house.y2 + house.freeSpace, 0.5):
                try:
                    plan.coordinates.remove([x, y])
                except ValueError:
                    pass

    print("ready for output")
    output.Output(plan)   

if __name__ == "__main__":
    greedy(60)