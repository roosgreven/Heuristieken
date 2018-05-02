"""
Finds distance between given house and house or boundary closest to that house.  
Takes in the array of placed houses and the house to check.  Distance will be 
negative when two houses overlap.
"""

import helpers.shortestdistance as sd
from classes.floorplan import FloorPlan

def findClosestHouse(houses, chosenHouse):
    """ Finds the closes distance of a house to another house or a boundary.
    Takes in the array of houses and the house that will be checked.
    """

    # Set distance to max
    distance = FloorPlan.width


    # Loop over all houses
    for house in houses:
        
        # Check if house is not chosenHouse
        if not chosenHouse == house:
            
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


