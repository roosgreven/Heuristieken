import classes.houses as hs
import helpers.shortestdistance as sd
import helpers.findtotalvalue as ftv
import random
import matplotlib.pyplot as plt

def main():
    
    houses = []
    houseValues = []
    numberOfHouses = 20
    i = 0
    overlaps = 0
    
    while i < numberOfHouses:
        
        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)
        
        houses.append(hs.maison(x, y))

        if not(ftv.findTotalValue(houses, hs.maison(x, y))):
            print("overlap")
            overlaps += 1
            houses = houses[:-1]

        else:
            i += 1


    print("length houses: ", len(houses))
    print("# overlaps: ", overlaps)

    #houseValues.append(ftv.findTotalValue(houses, houses[i]))

    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]
    print(xlist)
    print(ylist)

    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    #plt.show()

if __name__ == "__main__":
    main()
