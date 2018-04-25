"""
Returns True when no overlap of houses exists
"""
import helpers.shortestdistance as sd

def noOverlap(houseArray, chosenHouse):

    if len(houseArray) > 1:

        # loop over all houses
        for house in houseArray:

            # check for overlap
            if sd.shortest(chosenHouse, house) < chosenHouse.freeSpace:
                return False

        return True

    # no overlap when there's only one house
    else:
        return True