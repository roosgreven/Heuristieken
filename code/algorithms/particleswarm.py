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
    
    # weighing factors for pBest and gBest
    c1, c2 = 0.0005, 0.0005
    
    for i in range(500):
        
        # The current overall best and all personal bests are updated
        population.checkForPAndGBest()
        
        # The initial gBest is saved to check if improvement was made
        if i == 0:
            population.firstGBest = population.gBest.getValue()
            
        # Each plan is updated
        for plan in population.plans:
            
            for j in range(plan.numberOfHouses):
                
                house = plan.houses[j]
                
                bestHouse = population.gBest.houses[j]
                
                # The increase in speed is determined for each house
                vx = c1 * random.random() * (house.xBest - house.x1) + c2 * random.random() * (bestHouse.x1 - house.x1)
                
                vy = c1 * random.random() * (house.yBest - house.y1) + c2 * random.random() * (bestHouse.y1 - house.y1)
                    
                # The speed is added and the coordinates updated
                house.speed(vx, vy)
                
                house.coordinates(house.x1 + house.vx, house.y1 + house.vy)
    
    return population      