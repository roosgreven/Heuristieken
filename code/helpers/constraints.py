"""
Contains three functions that check if the constraints are met.  noWater returns
False when the house overlaps with water, checkBoundaries returns False if there 
isn't enough free space for the house next to the neighbourhood boundaries.  
"""

import helpers.shortestdistance as sd
import helpers.findclosesthouse as fch

def noWaterAndBoundary(chosenObject, plan):
    """ Returns False if two houses overlap. """

    # Check for overlap with each pond
    for water in plan.ponds:

        distance = sd.shortest(water, chosenObject)
                
        # Check if water is inside house
        if distance < 0:

            return False
            
    # Checks left and lower boundary
    if chosenObject.x1 < chosenObject.freeSpace or chosenObject.y1 < chosenObject.freeSpace:
        return False

    # Checks right and upper boundary
    if chosenObject.x2 > plan.width - chosenObject.freeSpace or chosenObject.y2 > plan.length - chosenObject.freeSpace:
        return False

    return True

def checkIfPossible(house, plan):
    """ Checks if a house does not violate any constraints. """
    
    if noWaterAndBoundary(house, plan):
        
        distance = fch.findClosestHouse(plan, house)

        if distance > 0:
            
            return True
        
    return False