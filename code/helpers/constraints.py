"""
Contains two functions that check if the constraints are met. noOverlap returns
False when the house overlaps with another house, checkBoundaries returns False
if there isn't enough free space for the house next to the neighbourhood boundaries.
"""

import helpers.shortestdistance as sd

def noOverlap(houseArray, chosenHouse):
    """ Returns False if two houses overlap. """

    if len(houseArray) > 1:

        # Loop over all houses.
        for house in houseArray:

            # Check for overlap.
            if sd.shortest(chosenHouse, house) < chosenHouse.freeSpace:

                return False
        #print(chosenHouse)
        return True

    # No overlap when there's only one house.
    else:
        return True

def checkBoundaries(plan, house):
    """ Returns False if the house is too close to a boundary. """

    # Checks left and upper boundary.
    if house.x1 < house.freeSpace or house.y1 < house.freeSpace:
        return False

    # Checks right and lower boundary.
    if house.x2 > plan.width - house.freeSpace or house.y2 > plan.length - house.freeSpace:
        return False

    return True


def waterPlacement(plan, houseArray, water):
    """ Returns False if water cannot be placed """

    # Checks whether water fits within area boundaries
    if water.x2 > plan.width or water.y2 plan.length:
        return False

    if len(houseArray) > 1:

        # Loop over all houses
        for house in houseArray

            # Check if water is inside house
            if sd.shortest(water, house) < 0
                return False
