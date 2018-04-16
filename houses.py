ground = []

for i in range(20):
    ground.append([])
    for j in range(22):
        ground[i].append(0)

class house:
    def values(self, extraFreeSpace):
        self.totalExtraValue = self.extraValue * extraFreeSpace
        self.totalValue = self.basicValue + self.totalExtraValue
    
    def isEmpty(self, positionX, positionY):
        for meterLength in range(positionY, self.length + positionY):
            for meterWidth in range(positionX, self.width + positionX):
                if(ground[meterLength][meterWidth] != 0):
                    return

        for meterLength in range(positionY, self.length + positionY):
            for meterWidth in range(positionX, self.width + positionX):
                ground[meterLength][meterWidth] = self.theType

class eengezins(house):
    theType = 1
    width = 8
    length = 8
    basicValue = 285000
    freeSpace = 2
    extraValue = 0.3 * 285000

class bungalow(house):
    theType = 2
    width = 10
    length = 7
    basicValue = 399000
    freeSpace = 2
    extraValue = 0.4 * 399000

class maison(house):
    theType = 3
    width = 11
    length = 10
    basicValue = 610000
    freeSpace = 2
    extraValue = 0.6 * 610000

class water(house):
    def __init__(self, width, length):
        if ((width / length) < 0.25 or (width / length) > 4):
            raise ValueError
        self.width = width
        self.length = length
    theType = 4
