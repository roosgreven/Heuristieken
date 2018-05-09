"""
27 April 2018.

Contains a class with the floorplan for the neighbourhood.  This includes a list
with houses, a function to generate all coordinates and specifics for the
neighbourhood.
"""

import numpy as np
import csv
import random
import helpers.constraints as con
import classes.houses as hs
import classes.water as wt
import matplotlib.pyplot as plt
import helpers.findclosesthouse as fch

class FloorPlan:
    """ Has a list of houses and specifics for the neighbourhood """

    # The area of the neighbourhood
    width = 160.
    length = 180.
    numberOfPonds = 4

    # The specifics for all housetypes. Are also defined in the house classes,
    # but because there they are only available when there is an instance of
    # the house, they are also saved here. It's not very elegant and we will
    # change it at some point.
    eengezinsWidth = 8.
    eengezinsLength = 8.
    eengezinsFree = 2.

    bungalowWidth = 7.5
    bungalowLength = 10.
    bungalowFree = 3.

    maisonWidth = 10.5
    maisonLength = 11.
    maisonFree = 6.

    def __init__(self, houseNumber):

        # The total number of houses and number for each type
        self.numberOfHouses = houseNumber
        self.numberOfEengezins = int(self.numberOfHouses * 0.6)
        self.numberOfBungalows = int(self.numberOfHouses * 0.25)
        self.numberOfMaisons = int(self.numberOfHouses * 0.15)

        # The list of houses and the number of each type that are already placed
        self.houses = []
        self.currentEengezins = 0
        self.currentBungalows = 0
        self.currentMaisons = 0

        self.ponds =[]

    def createCoordinates(self):
        """ Creates a list of all possible coordinates in the neighbourhood.
        Coordinates too close to the boundary to ever place a house on them, are
        not added.
        """

        self.coordinates = []

        for x in np.arange(self.eengezinsFree, self.width - self.eengezinsFree - self.eengezinsWidth + 1, 0.5):
            for y in np.arange(self.eengezinsFree, self.length - self.eengezinsFree - self.eengezinsLength + 1, 0.5):
                self.coordinates.append([x, y])

    def makePonds(self):

        while len(self.ponds) < self.numberOfPonds:
            """ Place the ponds. """

            # Get random coordinates
            x, y = self.randomCoordinates()

            # Call water placement function
            self.waterPlacement(x, y)

    def waterPlacement(self, x, y):
        """ Places water at random location. x and y form the random coordinate. """

        # Initiate random water pond
        waterPond = wt.Pond(x, y)

        if con.noWaterAndBoundary(waterPond, self):

            self.ponds.append(waterPond)

    def randomCoordinates(self):
        """ Sets random coordinates x and y. """

        # Random coordinates
        x = round(random.random() * self.width, 1)
        y = round(random.random() * self.length, 1)
        return x, y

    def makeHouse(self, x, y):
        """ Initiates new house to place at position (x,y). """

        # Decide what type of house will be placed
        if len(self.houses) < self.numberOfMaisons:
            house = hs.Maison(x, y)

        elif len(self.houses) < self.numberOfMaisons + self.numberOfBungalows:
            house = hs.Bungalow(x, y)

        else:
            house = hs.Eengezins(x, y)

        if random.random() > 0.5:
            house.swap()

        return house

    def getValue(self):
        """ Total value of neighbourhood is calculated. """

        totalValue = 0

        for house in self.houses:

            totalValue += house.value(self)

        return totalValue


    def saveFloorplan(self):
        """ For now: Overwrites old floorplan with new one.

        Future: Checks if the value of the Floorplan is higher than the current value.  If so, the
        floorplan will overwrite the old floorplan.
        """

        # Initialize empty list
        coordinates = []

        totalValue = self.getValue()

        # Append total value to coordinates list
        coordinates.append(["totalValue", totalValue])

        # Add header rows to csv file
        coordinates.append(["Type", "x1", "x2", "y1", "y2"])

        # Iterate over ponds array of plan
        for pond in self.ponds:

            # Append coordinates of each pond to coordinates array
            coordinates.append(["Water", pond.x1, pond.x2, pond.y1, pond.y2])

        # Iterate over houses array in plan
        for house in self.houses:

            # Append coordinates of each house to coordinates array
            coordinates.append(["House",house.x1, house.x2, house.y1, house.y2])

        # Retrieved from https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
        myFile = open('houseplan.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(coordinates)

    def showFloorplan(self):
        """ Prints total value of a Floorplan and generates a visual floorplan
        with all houses and ponds. 
        """

        totalValue = 0

        print("Total houses placed:")
        print(len(self.houses))

        totalValue = self.getValue()

        print("The total value of the neighbourhood:")
        print(totalValue)

        # Visualisation of the floor plan
        plt.figure()

        # These coordinates together plot the outline of the neighbourhood
        xlist = [0, self.width, self.width, 0, 0]
        ylist = [0, 0, self.length, self.length, 0]
        plt.plot(xlist, ylist)

        for pond in self.ponds:

            # By plotting these lists, all corners will be connected by a line
            xlist = [pond.x1, pond.x2, pond.x2, pond.x1, pond.x1]
            ylist = [pond.y1, pond.y1, pond.y2, pond.y2, pond.y1]

            plt.plot(xlist, ylist)


        for house in self.houses:

            # By plotting these lists, all corners will be connected by a line
            xlist = [house.x1, house.x2, house.x2, house.x1, house.x1]
            ylist = [house.y1, house.y1, house.y2, house.y2, house.y1]

            print("a house")
            print(house.width)
            print(house.length)
            print(fch.findClosestHouse(self, house))

            plt.plot(xlist, ylist)

        plt.show()
