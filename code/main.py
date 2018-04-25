import classes.houses as hs
import helpers.shortestdistance as sd
import helpers.findclosesthouse as fch
import random
import matplotlib.pyplot as plt
import helpers.overlap as ov

def main():
    
    houses = []
    totalHouseValues = []
    numberOfHouses = 20
    i = 0

    # loop over houses
    while i < numberOfHouses:

        # get random coordinates
        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)

        randomHouse = hs.Maison(x, y)

        # check if there's overlap, if so, delete house from array and try again
        if ov.noOverlap(houses, randomHouse):
            # add house placed randomly
            houses.append(randomHouse)
            #totalHouseValues.append(houses[i].value(fch.findClosestHouse(houses, houses[i])))
            i += 1

    for house in houses:
        totalHouseValues.append(house.value(fch.findClosestHouse(houses, house)))
        print(round(house.value(fch.findClosestHouse(houses, house)),1))

    # add coordinates of houses to list
    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]

    # plot visualisation
    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    #plt.show()


if __name__ == "__main__":
    main()
