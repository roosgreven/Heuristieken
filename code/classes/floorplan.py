"""
27 April 2018.

Contains a class with the floorplan for the neighbourhood. This includes a list
with houses and specifics for the neighbourhood.
"""

class FloorPlan:
    """ Has a list of houses and specifics for the neighbourhood. """

    # The area of the neighbourhood.
    width = 160.
    length = 180.
    
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

        # The total number of houses and number for each type.
        self.numberOfHouses = houseNumber
        self.numberOfEengezins = int(self.numberOfHouses * 0.6)
        self.numberOfBungalows = int(self.numberOfHouses * 0.25)
        self.numberOfMaisons = int(self.numberOfHouses * 0.15)



        # The list of houses and the number of each type that are already placed.
        self.houses = []
        self.currentEengezins = 0
        self.currentBungalows = 0
        self.currentMaisons = 0

        self.ponds =[]
        
    def createCoordinates(self):
        
        self.coordinates = []
        
        for x in range(int(self.eengezinsFree), int(self.width - self.eengezinsFree - self.eengezinsWidth + 1)):
            for y in range(int(self.eengezinsFree), int(self.length - self.eengezinsFree - self.eengezinsLength + 1)):
            
                self.coordinates.append([x, y])
