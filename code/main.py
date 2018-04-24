<<<<<<< HEAD
import classes.houses as hs
import helpers.shortestdistance as sd
import random
import matplotlib.pyplot as plt
            
=======
import classes.houses
import classes.housetype as ht
import helpers.shortestdistance as sd
import random
import matplotlib.pyplot as plt

def findClosestHouse(houses, chosenHouse):
    distance = 160
    closestHouse = houses[0]

    for i in range(len(houses)):
        if i == chosenHouse:
            print('hallo')
            return
        if(sd.Shortest(chosenHouse, houses[i]) < distance):
            print(i)
            distance = sd.Shortest(chosenHouse, houses[i])
            closestHouse = houses[i]

    print(distance)

>>>>>>> 99354b0cefa8eb85a6b309541eae84512687509c
def main():

    houses = []
    numberOfHouses = 20

    for i in range(numberOfHouses):

        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)
<<<<<<< HEAD
        
        houses.append(hs.maison(x, y))
                   
=======

        houses.append(ht.maison(x, y))

>>>>>>> 99354b0cefa8eb85a6b309541eae84512687509c
    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]
    print(xlist)
    print(ylist)

    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    plt.show()

    findClosestHouse(houses, houses[0])
<<<<<<< HEAD
    
def findClosestHouse(houses, chosenHouse):
    distance = 160
    closestHouse = houses[0]
    
    for i in range(len(houses)):
        if i == chosenHouse:
            print('hallo')
            return
        if(sd.Shortest(chosenHouse, houses[i]) < distance):
            print(i)
            distance = sd.Shortest(chosenHouse, houses[i])
            closestHouse = houses[i]
            
    print(distance)
    
    
=======


>>>>>>> 99354b0cefa8eb85a6b309541eae84512687509c
if __name__ == "__main__":
    main()
