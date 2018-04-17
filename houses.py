totalHouses = 20
totalEengezins = int(totalHouses * 0.6)
totalBungalow = int(totalHouses * 0.25)
totalMaison = int(totalHouses * 0.15)
print totalEengezins
print totalBungalow
print totalMaison
ground = []
houses = []

def main():
    
    # create grid for the neighbourhood
    for i in range(50):
        ground.append([])
        for j in range(50):
            ground[i].append(0)
    
    for i in range(totalEengezins):
        houses.append(eengezins())
    
    for i in range(totalBungalow):
        houses.append(bungalow())
        
    for i in range(totalMaison):
        houses.append(maison())
        
    for house in houses:
        switch = False
        for i in range(50):
            for j in range(50):
                if(house.checkIfEmpty(j,i)):
                    house.placeObject(j,i)
                    
                    switch = True
                    break
            if switch == True:
                break
    
    """"
    one = eengezins()
    if(one.checkIfEmpty(2,2)):
        one.placeObject(2,2)
    """
    for row in ground:
        print row


# class for houses. Contains functions to calculate total value of house and to place a house if there's enough space.
class house:

    # calculate extra value and with that the total value
    def values(self, extraFreeSpace):
        self.totalExtraValue = self.extraValue * extraFreeSpace
        self.totalValue = self.basicValue + self.totalExtraValue

    # check if the spot at the given coordinates is empty
    def checkIfEmpty(self, positionX, positionY):

        # check if there's enough space for the house. If not, return from function.
        for meterWidth in range(positionX - self.freeSpace, self.width + self.freeSpace * 2 + positionX):
            for meterLength in range(positionY - self.freeSpace, self.length + self.freeSpace * 2 + positionY):

                if(meterLength > 50 - self.freeSpace or meterWidth > 50 - self.freeSpace): 
                    return 
                elif(ground[meterLength][meterWidth] != 0):
                    return False

        return True

    # place object on given coordinates
    def placeObject(self, positionX, positionY):
        # place house on grid
        for meterWidth in range(positionX, self.width + positionX):
            for meterLength in range(positionY, self.length + positionY):
                ground[meterLength][meterWidth] = self.theType

        # place free space at north and south sides of the house
        for meters in range(self.width):
            for metersFreeSpace in range(self.freeSpace):
                ground[positionY + self.length + metersFreeSpace][meters + positionX] = self.freeSpaceType
                if((positionY - (metersFreeSpace + 1)) >= 0):
                    ground[positionY - (metersFreeSpace + 1)][meters + positionX] = self.freeSpaceType


        # place free space at east and west sides of the house
        for meters in range(self.length):
            for metersFreeSpace in range(self.freeSpace):
                ground[positionY + meters][positionX + self.width + metersFreeSpace] = self.freeSpaceType
                if((positionX - 1 - metersFreeSpace) >= 0):
                    ground[positionY + meters][positionX - 1 - metersFreeSpace] = self.freeSpaceType


class eengezins(house):
    theType = 1
    width = 3
    length = 3
    basicValue = 285000
    freeSpace = 1
    freeSpaceType = 2
    extraValue = 0.3 * 285000

class bungalow(house):
    theType = 3
    width = 5
    length = 4
    basicValue = 399000
    freeSpace = 1
    freeSpaceType = 4
    extraValue = 0.4 * 399000

class maison(house):
    theType = 5
    width = 7
    length = 6
    basicValue = 610000
    freeSpace = 1
    freeSpaceType = 6
    extraValue = 0.6 * 610000

class water(house):
    theType = 7
    def __init__(self, width, length):
        if ((width / length) < 0.25 or (width / length) > 4):
            raise ValueError
        self.width = width
        self.length = length
        
if __name__ == "__main__":
    main()

totalHouses = 20
totalEengezins = totalHouses * 0.6
totalBungalow = totalHouses * 0.25
totalMaison = totalHouses * 0.15

one = eengezins()
if(one.checkIfEmpty(2,2)):
    one.placeObject(2,2)

for row in ground:
    print row
