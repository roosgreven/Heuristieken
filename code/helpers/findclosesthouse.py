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
    for i in range(len(houses)):

        # check if house is not chosen house
        if(chosenHouse.x1 != houses[i].x1 and chosenHouse.x2 != houses[i].x2):

            # check for overlap
            if(sd.Shortest(chosenHouse, houses[i]) > chosenHouse.freeSpace):

                # check if distance between two houses is smaller than previous smallest distance
                if(sd.Shortest(chosenHouse, houses[i]) < distance):

                    # save new smallest distance
                    distance = sd.Shortest(chosenHouse, houses[i])
                    closestHouse = houses[i]

            # return false if there's overlap
            else:
                return False

    # return smallest distance
    return(distance)