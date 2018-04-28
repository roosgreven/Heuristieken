"""
Contains two functions that check if the constraints are met. noOverlap returns
False when the house overlaps with another house, checkBoundaries returns False
if there isn't enough free space for the house next to the neighbourhood boundaries.
"""

import helpers.shortestdistance as sd
import classes.water as wt
from classes.floorplan import FloorPlan

def noOverlap(houseArray, chosenHouse, ponds):
    """ Returns False if two houses overlap. """

    if len(houseArray) > 1:

        # Loop over all houses.
        for house in houseArray:

            # Check for overlap.
            if sd.shortest(chosenHouse, house) < chosenHouse.freeSpace:

                return False

            # Check for each water pond
            for water in ponds:

                # Check if water is inside house
                if sd.shortest(water, chosenHouse) < 0:

                    return False


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
