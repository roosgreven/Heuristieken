"""
24 April 2018.

Contains a house class for each house with coordinates and value.  Contains
subclasses for each housetype with specific values.  Each housetype inherits
from the house class.
"""
import helpers.findclosesthouse as fch

class House:
    """ Keeps up with the coordinates and value of a house. """

    def __init__(self, x1, y1):

        self.coordinates(x1, y1)

    def value(self, plan):
        """ Takes in the array of houses and uses it to calculate the shortest
        distance for the house.  Then calculates and returns the house value.
        """
        
        distance = fch.findClosestHouse(plan, self)
        
        if distance < 0:
            return -1
        
        extraFreeSpace = distance - self.freeSpace
        totalValue = self.basicValue + self.extraValue * extraFreeSpace
        
        return totalValue

    def coordinates(self, x1, y1):
        """ Calculates the houses coordinates. To do this it only needs x1 and 
        y1, the coordinate of the lower left corner. 
        """

        self.x1 = x1
        self.x2 = x1 + self.width
        self.y1 = y1
        self.y2 = y1 + self.length
        
    def swap(self):
        """ Swaps the value of width and length and changes coordinates
        accordingly. """
        
        self.width, self.length = self.length, self.width
        
        self.coordinates(self.x1, self.y1)

class Eengezins(House):
    """ Specifies the "eengezins" housetype. Inherits from house(). """

    width = 8.
    length = 8.
    basicValue = 285000.
    freeSpace = 2.
    extraValue = 0.03 * basicValue

    def __init__(self, x1, y1):
        House.__init__(self, x1, y1)

class Bungalow(House):
    """ Specifies the "bungalow" housetype. Inherits from house(). """

    width = 7.5
    length = 10.
    basicValue = 399000.
    freeSpace = 3.
    extraValue = 0.04 * basicValue

    def __init__(self, x1, y1):
        House.__init__(self, x1, y1)

class Maison(House):
    """ Specifies the "maison" housetype. Inherits from house(). """

    width = 10.5
    length = 11.
    basicValue = 610000.
    freeSpace = 6.
    extraValue = 0.06 * basicValue

    def __init__(self, x1, y1):
        House.__init__(self, x1, y1)
