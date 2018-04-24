""" 
Contains a house class for each house with coordinates and value.  Contains 
subclasses for each housetype with specific values.  Each housetype inherits
from the house class.
"""

class house:
    """ Keeps up with the coordinates and value of a house. """
    
    def __init__(self, x1, y1):
        
        self.coordinates(x1, y1)
        self.totalValue = self.basicValue
        
    def value(self, distance):
        """ Calculates the value of a house for the given shortest distance. """
        
        extraFreeSpace = distance - self.freeSpace
        
        self.totalValue = self.basicValue + self.extraValue * extraFreeSpace
        
    def coordinates(self, x1, y1):
        """ Calculates the houses coordinates. """
        
        self.x1 = x1
        self.x2 = x1 + self.width
        self.y1 = y1
        self.y2 = y1 + self.length
        
class eengezins(house):
    """ Specifies the "eengezins" housetype. Inherits from house(). """
    
    width = 8
    length = 8
    basicValue = 285000
    freeSpace = 2
    extraValue = 0.03 * basicValue
    
    def __init__(self, x1, y1):
        house.__init__(self, x1, y1)

class bungalow(house):
    """ Specifies the "bungalow" housetype. Inherits from house(). """
    
    width = 7.5
    length = 10
    basicValue = 399000
    freeSpace = 3
    extraValue = 0.04 * basicValue
    
    def __init__(self, x1, y1):
        house.__init__(self, x1, y1)
        
class maison(house):
    """ Specifies the "maison" housetype. Inherits from house(). """
    
    width = 10.5
    length = 11
    basicValue = 610000
    freeSpace = 6
    extraValue = 0.06 * basicValue
    
    def __init__(self, x1, y1):
        house.__init__(self, x1, y1)