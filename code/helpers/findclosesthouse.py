"""
Finds distance between given house and house or boundary closest to that house.  
Takes in the array of placed houses and the house to check.  Distance will be 
negative when two houses overlap.
"""

import helpers.shortestdistance as sd

def findClosestHouse(plan, chosenHouse):
    """ Finds the closes distance of a house to another house or a boundary.
    
    Arg1: 
        plan: current floorplan.

    Arg2:
        house: house to check.

    Return:
        -1: if house is too close to other house
        distance: distance to closest house.
        
    """

    # Set distance to max
    distance = plan.width

    # Loop over all houses
    for house in plan.houses:
        
        # Check if house is not chosenHouse
        if not chosenHouse == house:
            
            newDistance = sd.shortest(chosenHouse, house)
            
            # Check if house is outside other house's freespace
            if newDistance < house.freeSpace:
                
                return -1

            # Check if distance between two houses is smaller than previous smallest distance
            if newDistance < distance:

                # Save new smallest distance
                distance = newDistance

    # Check if distance between house and border is smaller than previous smallest distance
    if chosenHouse.x1 < distance:

        distance = chosenHouse.x1

    if plan.width - chosenHouse.x2 < distance:

        distance = plan.width - chosenHouse.x2

    if chosenHouse.y1 < distance:

        distance = chosenHouse.y1

    if plan.length - chosenHouse.y2 < distance:

        distance = plan.length - chosenHouse.y2
        
    if distance < chosenHouse.freeSpace:
        
        return -1

    # Return smallest distance
    return distance


