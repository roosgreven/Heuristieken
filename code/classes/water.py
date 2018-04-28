class Water:
    def __init__(self, x1, y1, width, length):

        self.coordinates(x1, y1)
        self.width = 20
        self.length = 72
        self.ponds = []

    def coordinates(self, x1, y2):
        """ Calculates the houses coordinates. """

        self.x1 = x1
        self.x2 = x1 + self.width
        self.y2 = y2
        self.y1 = y2 - self.length
