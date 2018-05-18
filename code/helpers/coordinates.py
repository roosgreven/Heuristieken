"""
Finds the best coordinate for a house.
"""

import helpers.constraints as con
import helpers.findclosesthouse as fch
import numpy as np

def findCoordinates(plan, house):
    """ Finds the best coordinate to place the house. """
    
    bestX, bestY = 0, 0
    distance = 0
    
    # Looks for the best coordinate to place a house
    for coordinate in plan.coordinates:

        x, y = coordinate[0], coordinate[1]

        # The house is set to new coordinate
        house.coordinates(x, y)

        # Check if it can be placed there
        if con.noWaterAndBoundary(house, plan):

            # Find closest distance to house or border
            newDistance = fch.findClosestHouse(plan, house)

            # If there's more freespace in this position, take over coordinates
            if newDistance > distance:

                distance = newDistance
                bestX, bestY = x, y
                
    return bestX, bestY, distance
    
def removeCoordinates(plan, house):
    """ All coordinates that are unavailable because of the house, are removed 
    from the list of coordinates.
    """
    
    for x in np.arange(house.x1 - house.freeSpace - plan.smallestLength + 1, house.x2 + house.freeSpace, 0.5):
        for y in np.arange(house.y1 - house.freeSpace - plan.smallestLength + 1, house.y2 + house.freeSpace, 0.5):
            try:
                plan.coordinates.remove([x, y])
            except ValueError:
                pass 