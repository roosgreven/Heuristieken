"""
Returns True when no overlap of houses exists
"""
import helpers.shortestdistance as sd

def noOverlap(houseArray, chosenHouse):

    if len(houseArray) > 1:

        # loop over all houses
        for house in houseArray:

            # check if house is not chosen house
            if chosenHouse.x1 != house.x1 and chosenHouse.x2 != house.x2:

                # check for overlap
                return sd.shortest(chosenHouse, house) > chosenHouse.freeSpace
    else:
        return True