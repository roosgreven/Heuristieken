"""
27 April 2018.

Contains a class with the floorplan for the neighbourhood.   This includes a list
with houses and specifics for the neighbourhood.
"""

class FloorPlan:
    """ Has a list of houses and specifics for the neighbourhood. """

    # The area of the neighbourhood.
    width = 160
    length = 180

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
