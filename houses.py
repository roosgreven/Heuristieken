ground = []

for i in range(160 * 2):
    ground.append([])
    for j in range(180 * 2):
        ground[i].append(0)

class house:
    def values(self, extraFreeSpace):
        self.totalExtraValue = self.extraValue * extraFreeSpace
        self.totalValue = self.basicValue + self.totalExtraValue

class eengezins(house):
    width = 8
    length = 8
    basicValue = 285000
    freeSpace = 2
    extraValue = 0.3 * 285000

class bungalow(house):
    width = 10
    length = 7.5
    basicValue = 399000
    freeSpace = 2
    extraValue = 0.4 * 399000

class maison(house):
    width = 11
    length = 10.5
    basicValue = 610000
    freeSpace = 2
    extraValue = 0.6 * 610000

class water:
    def __init__(self, width, length):
        if ((width / length) < 0.25 or (width / length) > 4):
            raise ValueError