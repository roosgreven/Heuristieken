import classes.houses as hs
import helpers.shortestdistance as sd
import helpers.findclosesthouse as fch
import random
import matplotlib.pyplot as plt

def main():
    
    houses = []
    totalHouseValues = []
    numberOfHouses = 20
    i = 0
    overlaps = 0
    
    while i < numberOfHouses:
        
        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)
        
        houses.append(hs.maison(x, y))

        if not(fch.findClosestHouse(houses, hs.maison(x, y))):

            houses = houses[:-1]

        else:
            totalHouseValues.append(houses[i].value(fch.findClosestHouse(houses, houses[i])))
            i += 1

    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]

    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    #plt.show()

if __name__ == "__main__":
    main()
