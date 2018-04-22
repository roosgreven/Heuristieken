import housetype as ht
import shortestdistance as sd
import random
import matplotlib.pyplot as plt

def main():
    
    houses = []
    
    for i in range(20):
        
        x = random.random() * 160
        y = random.random() * 180
        
        houses.append(ht.maison(x, y))
    
    for i in range(20):
        
        print(i)
        
        for j in range(20):
            
            if not i == j:
                
                distance = sd.Shortest(houses[i], houses[j])
                houses[i].value(distance)
                print(houses[i].totalValue)
                
    xlist = [house.x1 for house in houses]
    ylist = [house.y1 for house in houses]
    print xlist
    print ylist
    
    plt.figure()
    plt.plot(xlist, ylist, 'bo')
    plt.show()
    
if __name__ == "__main__":
    main()