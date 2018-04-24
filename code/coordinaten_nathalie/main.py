import housetype as ht
import shortestdistance as sd
import random
import matplotlib.pyplot as plt

def findClosestHouse(houses, chosenHouse):
    distance = 160
    closestHouse = houses[0]
    
    for i in range(len(houses)):
        if i == closestHouse:
            print('hallo')
        if(sd.Shortest(chosenHouse, houses[i]) < distance):
            distance = sd.Shortest(chosenHouse, houses[i])
            closestHouse = houses[i]
            
    print(distance)
            
def main():
    
    houses = []
    numberOfHouses = 20
    
    for i in range(numberOfHouses):
        
        x = round(random.random() * 160, 1)
        y = round(random.random() * 180, 1)
        
        houses.append(ht.maison(x, y))
                   
    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]
    print(xlist)
    print(ylist)
    
    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    plt.show()
    
    findClosestHouse(houses, houses[0])
    
    
if __name__ == "__main__":
    main()
    
