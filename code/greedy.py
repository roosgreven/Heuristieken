"""
29 April 2018.

Contains a greedy algorithm to solve Amstelhaege. It generates a list with all
possible coordinates a house can have and iterates through this list for every
house to find the highest value place. But, whenever a house gets placed, this
reduces the number of places the next house has. The coordinates that are
impossible then get removed form the list.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import helpers.constraints as con
import classes.water as wt
import helpers.output as output
import random

def greedy(houseNumber):
    
    plan = FloorPlan(houseNumber)

    plan.createCoordinates()

    # First house hasn't been placed yet
    firstHouse = False

    while firstHouse == False:

        # Get random coordinates
        x = round(random.random() * plan.width, 1)
        y = round(random.random() * plan.length, 1)

        # Create house
        house1 = hs.Maison(x, y)

        # Check if coordinates don't cross boundaries
        if con.checkBoundaries(plan, house1):

            # Save house with these coordinates
            plan.houses.append(house1)
            firstHouse = True

    # Places the houses with a greedy algorithm
    for i in range(houseNumber - 1):
        
        # Decide what type of house will be placed. A testhouse is also made to
        # check for each coordinate if it's better than the current one. If it is,
        # the better coordinate will be saved
        
        if i < plan.numberOfMaisons - 1:
            
            house = hs.Maison(0, 0)
            testHouse = hs.Maison(0, 0)
            plan.currentMaisons += 1
            print('maison')

        elif i < plan.numberOfMaisons + plan.numberOfBungalows - 1:

            house = hs.Bungalow(0, 0)
            testHouse = hs.Bungalow(0, 0)
            plan.currentBungalows += 1
            print("bungalow")

        else:
            house = hs.Eengezins(0, 0)
            testHouse = hs.Eengezins(0, 0)
            plan.currentEengezins += 1
            print("eengezins")
            
        distance = 0

        # Looks for the best coordinate to place a house
        for coordinate in plan.coordinates:

            x, y = coordinate[0], coordinate[1]

            # The testhouse is set to new coordinate
            testHouse.coordinates(x, y)

            # Check if it can be placed there
            if con.checkBoundaries(plan, testHouse):
                if con.noOverlap(plan.houses, testHouse, plan.ponds):

                    # Find closest distance to house or border
                    newDistance = fch.findClosestHouse(plan.houses, testHouse)

                    # If there's more freespace in this position, take over coordinates
                    if newDistance > distance:

                        distance = newDistance
                        house.coordinates(x, y)
        print("distance: ", distance)
        plan.houses.append(house)
        print("house ", len(plan.houses))

        # All coordinates that have guaranteed become unavailable because of the
        # house that was just placed, are removed from the list of coordinates
        for x in range(int(house.x1 - house.freeSpace - plan.eengezinsWidth + 1), int(house.x2 + house.freeSpace)):
            for y in range(int(house.y1 - house.freeSpace - plan.eengezinsLength + 1), int(house.y2 + house.freeSpace)):

                if [x, y] in plan.coordinates:
                    plan.coordinates.remove([x, y])

    print("ready for output")
    output.Output(plan)   

if __name__ == "__main__":
    greedy(20)