import helpers.shortestdistance as sd

"""
Finds distance between given house and house closest to that house. 
Takes in the array of placed houses and the house to check. 
Returns false if there's overlap between houses. 
Returns distance if there's no overlap. 
"""

def findClosestHouse(houses, chosenHouse):

    # set distance to fake number
    distance = 160

    # loop over all houses
    for house in houses:

        # check if house is not chosen house
        if chosenHouse.x1 != house.x1 and chosenHouse.x2 != house.x2:

            print(sd.shortest(chosenHouse, house))

            # check if distance between two houses is smaller than previous smallest distance
            if sd.shortest(chosenHouse, house) < distance:

                # save new smallest distance
                distance = sd.shortest(chosenHouse, house)
                closestHouse = house

    # return smallest distance
    return distance


