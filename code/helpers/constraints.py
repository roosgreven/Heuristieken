"""
Contains two functions that check if the constraints are met. noOverlap returns
False when the house overlaps with another house, checkBoundaries returns False
if there isn't enough free space for the house next to the neighbourhood boundaries.
"""

import helpers.shortestdistance as sd
#import classes.water as wt
#from classes.floorplan import FloorPlan

def noOverlap(houseArray, chosenHouse, ponds):
    """ Returns False if two houses overlap. """

    # Loop over all houses
    for house in houseArray:

        # Check if house is not chosen house
        if chosenHouse.x1 != house.x1 and chosenHouse.x2 != house.x2:
            distance = sd.shortest(chosenHouse, house)

            # Check for overlap
            if distance < chosenHouse.freeSpace or distance < house.freeSpace:


                return False

    # Check for overlap with each pond
    for water in ponds:

        distance = sd.shortest(water, chosenHouse)
                
        # Check if water is inside house
        if distance < 0:

            return False

    return True

def checkBoundaries(plan, house):
    """ Returns False if the house is too close to a boundary. """

    # Checks left and lower boundary
    if house.x1 < house.freeSpace or house.y1 < house.freeSpace:
        return False

    # Checks right and upper boundary
    if house.x2 > plan.width - house.freeSpace or house.y2 > plan.length - house.freeSpace:
        return False

    return True
    
def waterCheck(plan, water):
    """ Returns False if the water is outside a boundary or inside another pond. """
    
    if len(plan.ponds) > 0:
        
        # Loop over all ponds
        for pond in plan.ponds:
            
            distance = sd.shortest(water, pond)
            
            # Check for overlap
            if distance < 0:
                
                return False
                
    # Checks if water is within the neighbourhood boundaries. Since x1 and y1
    # are generated within the neighbourhood, water can only cross the right and
    # upper boundary
    if water.x2 > plan.width or water.y2 > plan.length:
        return False

    return True