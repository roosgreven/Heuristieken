"""
27 April 2018.

Contains a class with the floorplan for the neighbourhood.  This includes a list
with houses, a function to generate all coordinates and specifics for the 
neighbourhood.
"""

import numpy as np

class FloorPlan:
    """ Has a list of houses and specifics for the neighbourhood """

    # The area of the neighbourhood
    width = 160.
    length = 180.
    
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
