"""
Finds distance between given house and house closest to that house. 
Takes in the array of placed houses and the house to check. 
Returns false if there's overlap between houses. 
Returns distance if there's no overlap. 
"""

import helpers.shortestdistance as sd
from classes.floorplan import FloorPlan

def findClosestHouse(houses, chosenHouse):

    # Set distance to max
    distance = FloorPlan.width


    # Loop over all houses
    for house in houses:

        # Check if house is not chosen house
        if chosenHouse.x1 != house.x1 and chosenHouse.x2 != house.x2:
            
            newDistance = sd.shortest(chosenHouse, house)

            # Check if distance between two houses is smaller than previous smallest distance
            if newDistance < distance:

                # Save new smallest distance
                distance = newDistance

    # Check if distance between house and border is smaller than previous smallest distance
    if chosenHouse.x1 < distance:

        distance = chosenHouse.x1

    if FloorPlan.width - chosenHouse.x2 < distance:

        distance = FloorPlan.width - chosenHouse.x2

    if chosenHouse.y1 < distance:

        distance = chosenHouse.y1

    if FloorPlan.length - chosenHouse.y2 < distance:

        distance = FloorPlan.length - chosenHouse.y2

    # Return smallest distance
    return distance


