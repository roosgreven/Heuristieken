import helpers.shortestdistance as sd

def findTotalValue(houses, chosenHouse):

    distance = 160
    for i in range(len(houses)):
        if(chosenHouse.x1 != houses[i].x1 and chosenHouse.x2 != houses[i].x2):
            if(sd.Shortest(chosenHouse, houses[i]) > chosenHouse.freeSpace):
                if(sd.Shortest(chosenHouse, houses[i]) < distance):
                    distance = sd.Shortest(chosenHouse, houses[i])
                    closestHouse = houses[i]
            else:
                return False

    chosenHouse.value(distance)

    return(distance)