# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:35:11 2018

Performs a particle swarm algorithm.  There's multiple floorplans, each house
of each floorplan has a speed that depends on the overall best value and the
floorplans personal best value.  The speed is used to update the population
and direct it to the best possible solution.
"""

import random

def particleSwarm(population):
    """ Performs the algorithm. """
    
    c1, c2 = 0.0005, 0.0005
    
    for i in range(500):
        
        # The current overall best is established
        population.checkForPAndGBest()
        
        if i == 0:
            population.firstFBest = population.gBest.getValue()
            
        for plan in population.plans:
            
            for j in range(plan.numberOfHouses):
                
                house = plan.houses[j]
                
                #print(house.vx, house.vy)
                
                bestHouse = population.gBest.houses[j]
                """
                if counter == 0:
                    
                    print("een iteratie")
                    print(bestHouse.x1)
                    print(bestHouse.vx)
                    print(house.xBest)
                    print(house.x1)
                    print(house.vx)
                    print(c1 * random.random() * (house.xBest - house.x1))
                    print(c2 * random.random() * (bestHouse.x1 - house.x1))
                counter += 1
                """
                vx = c1 * random.random() * (house.xBest - house.x1) + c2 * random.random() * (bestHouse.x1 - house.x1)
                
                vy = c1 * random.random() * (house.yBest - house.y1) + c2 * random.random() * (bestHouse.y1 - house.y1)
                    
                house.speed(vx, vy)
                
                house.coordinates(house.x1 + house.vx, house.y1 + house.vy)
    
    return population
    """
    print("the horrible house")
    for house in population.plans[0].houses:
        
        print(house.vx)
        print(house.vy)
        
    print("the best house")
    for house in population.gBest.houses:
        
        print(house.vx)
        print(house.vy)
                
    """