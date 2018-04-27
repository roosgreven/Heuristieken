"""
Finds distance between given house and house closest to that house. 
Takes in the array of placed houses and the house to check. 
Returns false if there's overlap between houses. 
Returns distance if there's no overlap. 
"""

import helpers.shortestdistance as sd

def findClosestHouse(houses, chosenHouse):

    # Set distance to fake number.
    distance = 160.

    # Loop over all houses.
    for house in houses:

        # Check if house is not chosen house.
        if chosenHouse.x1 != house.x1 and chosenHouse.x2 != house.x2:

            # Check if distance between two houses is smaller than previous smallest distance.
            if sd.shortest(chosenHouse, house) < distance:

                # Save new smallest distance.
                distance = sd.shortest(chosenHouse, house)
                closestHouse = house

    # Return smallest distance.
    return distance


