import classes.houses as hs
import helpers.shortestdistance as sd
import helpers.findtotalvalue as ftv
import random
import matplotlib.pyplot as plt

def main():
    
    houses = []
    numberOfHouses = 20
    
    for i in range(numberOfHouses):
        
        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)
        
        houses.append(hs.maison(x, y))

    ftv.findTotalValue(houses, houses[0])

    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]
    print(xlist)
    print(ylist)

    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    plt.show()

if __name__ == "__main__":
    main()
