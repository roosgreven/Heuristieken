import classes.houses as hs
import helpers.shortestdistance as sd
import helpers.findclosesthouse as fch
import random
import matplotlib.pyplot as plt
import helpers.overlap as ov

def main():

    numberOfHouses = 20
    numberOfEengezins = numberOfHouses * 0.6
    currentEengezins = 0
    currentBungalows = 0
    currentMaisons = 0
    numberOfBungalows = numberOfHouses * 0.25
    numberOfMaisons = numberOfHouses * 0.15
    houses = []

    i = 0
    totalValue = 0
    totalHouseValues = []

    # loop over houses
    while i < numberOfHouses:

        # get random coordinates
        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)

        if len(houses) < numberOfEengezins:
            randomHouse = hs.Eengezins(x, y)
            currentEengezins += 1
        elif len(houses) < numberOfEengezins + numberOfBungalows:
            randomHouse = hs.Bungalow(x, y)
            currentBungalows += 1
        else:
            randomHouse = hs.Maison(x, y)
            currentMaisons += 1

        # check if there's overlap, if so, delete house from array and try again
        if ov.noOverlap(houses, randomHouse):

            # add placed randomly house
            houses.append(randomHouse)
            i += 1

    # add coordinates of houses to list
    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]

    # plot visualisation
    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    plt.show()


if __name__ == "__main__":
    main()
