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

    # loop over houses
    while i < numberOfHouses:

        # get random coordinates
        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)

        # add house placed randomly
        houses.append(hs.maison(x, y))

        # check if there's overlap, if so, delete house from array and try again
        if not(fch.findClosestHouse(houses, hs.maison(x, y))):
            houses = houses[:-1]

        # add value of house to array and continue if no overlap
        else:
            totalHouseValues.append(houses[i].value(fch.findClosestHouse(houses, houses[i])))
            i += 1

    # add coordinates of houses to list
    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]

    # plot visualisation
    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    #plt.show()

if __name__ == "__main__":
    main()
