class Water:
    def __init__(self, x1, y1):

        self.coordinates(x1, y1)


    def coordinates(self, x1, y2):
        """ Calculates the houses coordinates. """

        self.x1 = x1
        self.x2 = x1 + self.width
        self.y2 = y2
        self.y1 = y2 - self.length

class Pond(Water):
        width = 20.
        length = 72.
        def __init__(self, x1, y1):
            Water.__init__(self, x1, y1)
