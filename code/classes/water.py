"""
28 April 2018.

Contains a Water class that keeps up with the coordinates of each pond.  Also
contains a Pond class with the specifics for a pond.
"""

class Water:
    """ Contains the coordinates of a pond """
    
    def __init__(self, x1, y1):

        self.coordinates(x1, y1)


    def coordinates(self, x1, y1):
        """ Calculates the waters coordinates """

        self.x1 = x1
        self.x2 = x1 + self.width
        self.y1 = y1
        self.y2 = y1 + self.length

class Pond(Water):
    """ Contains the specifics of a pond """
    
    width = 20.
    length = 72.
    freeSpace = 0.
    def __init__(self, x1, y1):
        Water.__init__(self, x1, y1)
