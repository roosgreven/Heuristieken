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
    
    c1, c2 = 0.05, 0.005
    
    population.plans[0].showFloorplan()
    
    for i in range(500):
        
        # The current overall best is established
        population.checkForPAndGBest()
        
        #if i == 0:
            #population.gBest.showFloorplan()
        
        for plan in population.plans:
            
            for j in range(plan.numberOfHouses):
                
                house = plan.houses[j]
                
                #print(house.vx, house.vy)
                
                bestHouse = population.gBest.houses[j]
                
                vx = house.vx + c1 * random.random() * (house.xBest - house.x1) + c2 * random.random() * (bestHouse.x1 - house.x1)
                
                vy = house.vy + c1 * random.random() * (house.yBest - house.y1) + c2 * random.random() * (bestHouse.y1 - house.y1)
                    
                house.speed(vx, vy)
                
                house.coordinates(house.x1 + house.vx, house.y1 + house.vy)
    population.plans[0].showFloorplan()
                
        