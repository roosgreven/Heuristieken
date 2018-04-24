import helpers.shortestdistance as sd

def findTotalValue(houses, chosenHouse):

    distance = 160

    for i in range(len(houses)):
        if((houses[i].x1 != chosenHouse.x1) and (houses[i].x2 != chosenHouse.x2)):
            if(sd.Shortest(chosenHouse, houses[i]) < distance):
                distance = sd.Shortest(chosenHouse, houses[i])
                closestHouse = houses[i]

    chosenHouse.value(distance)

    return(chosenHouse.value(distance))