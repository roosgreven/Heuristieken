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

class FloorPlan:
    """ Has a list of houses and specifics for the neighbourhood. """

    # The area of the neighbourhood
    width = 160.
    length = 180.
    numberOfPonds = 4

    # The smallest freespace (eengezins), combination of freespace and length
    # (eengezins) and length (bungalow). Used to remove coordinates where a
    # house can"t possibly be placed
    smallestFree = 2.
    smallestLengthPlusFree = 8. + smallestFree
    smallestLength = 7.5

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
        
        # Initiates the pBestValue for the particle swarm algorithm
        self.pBestValue = 0

    def createCoordinates(self):
        """ Creates a list of all possible coordinates in the neighbourhood.
        Coordinates too close to the boundary to ever place a house on them, are
        not added.
        """

        self.coordinates = []

        for x in np.arange(self.smallestFree, self.width - self.smallestFree - self.smallestLengthPlusFree + 1, 0.5):
            for y in np.arange(self.smallestFree, self.length - self.smallestFree - self.smallestLengthPlusFree + 1, 0.5):
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
            house.rotate()

        return house
    
    def checkWaterAndBoundary(self):
        
        for house in self.houses:
            
            if not con.noWaterAndBoundary(house, self):
                
                return False
        
        return True

    def getValue(self):
        """ Total value of neighbourhood is calculated. """

        totalValue = 0

        for house in self.houses:

            totalValue += house.value(self)

        return totalValue
    
    def changeBest(self):
        """ The best x1 and y1 value are updated for each house. Used in the
        particle swarm algorithm.
        """
        
        for house in self.houses:
            
            house.changeBest()
        
    def saveFloorplan(self, algorithmType, numberOfHouses):
        """ Checks if the value of the Floorplan is higher than the current best value.  If so, the
        floorplan will overwrite the old floorplan.
        """

        totalValue = self.getValue()

        # Open file specific for this algorithm and this number of houses
        with open("code/results/" + algorithmType + "_" + str(numberOfHouses) + ".csv", "r") as myFile:
            
            # read CSV file and save best value ever achieved
            reader = csv.reader(myFile, delimiter = ",")
            bestThisAlgorithm = float(list(reader)[0][1])

        # Check if this value is better than best ever achieved
        if bestThisAlgorithm < totalValue: 

            # Initialize empty list
            coordinates = []

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
                coordinates.append(["House", house.x1, house.x2, house.y1, house.y2])

            # Open and read file with all highscores
            with open("code/results/allBests.csv", "r") as myFile:
                reader = csv.reader(myFile, delimiter = ",")
                
                # List the file
                listedValues = list(reader)

            # Loop over all items in the file
            for item in listedValues:

                # Change total value of specific algorithm
                if item[0] == algorithmType + "_" + str(numberOfHouses):
                    item[1] = totalValue

            # Open file with all best values to write score to
            with open("code/results/allBests.csv", "w", newline = "") as myFile:
                writer = csv.writer(myFile)

                # Write the changed values
                writer.writerows(listedValues)

            # Open csv for specific algorithm to write new floorplan to
            with open("code/results/" + algorithmType + "_" + str(numberOfHouses) + ".csv", "w", newline = "") as myFile:
                writer = csv.writer(myFile)

                # Write total value and coordinates of houses and water to csv
                writer.writerows(coordinates)

            # Open file with best value ever achieved
            with open("code/results/bestEver.csv", newline = "") as csvfile:
                
                # Check save best value ever achieved
                reader = csv.reader(csvfile, delimiter=",")
                bestTillNow = float(list(reader)[0][1])

            # If this value is best ever achieved, save it in the csvfile
            if bestTillNow < totalValue: 

                with open("code/results/bestEver.csv", "w") as myFile:
                    writer = csv.writer(myFile)

                    # Write total value and coordinates of houses and water to csv
                    writer.writerows(coordinates + [["Algorithm Type: " + algorithmType]] 
                        + [["Number of Houses: " + str(numberOfHouses)]])
       

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
        plt.plot(xlist, ylist, "m-")

        for pond in self.ponds:

            # By plotting these lists, all corners will be connected by a line
            xlist = [pond.x1, pond.x2, pond.x2, pond.x1, pond.x1]
            ylist = [pond.y1, pond.y1, pond.y2, pond.y2, pond.y1]

            plt.plot(xlist, ylist, "b-")


        for house in self.houses:

            # By plotting these lists, all corners will be connected by a line
            xlist = [house.x1, house.x2, house.x2, house.x1, house.x1]
            ylist = [house.y1, house.y1, house.y2, house.y2, house.y1]
            
            color = "y-"

            if house.theType == "Eengezins":
                color = "r-"
            elif house.theType == "Bungalow":
                color = "g-"
            elif house.theType == "Maison":
                color = "c-"
                
            plt.plot(xlist, ylist, color)

        plt.show()
