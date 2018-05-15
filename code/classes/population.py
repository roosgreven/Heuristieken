# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:29:16 2018

Contains a class with floorplans in it.
"""

from randomalgorithm.randomalgorithm import randomAlgorithm
from classes.floorplan import FloorPlan

class Population:
    """ Has a list (a population) of floorplans. """
    
    def __init__(self, planNumber):
        
        self.planNumber = planNumber
        
        self.plans = []
        
    def makeRandomPopulation(self, houseNumber):
        
        self.velocity = []
        
        for i in range(self.planNumber):
            
            planVelocities = [[0, 0] for j in range(houseNumber)]
            self.velocity.append(planVelocities)
            
            plan = FloorPlan(houseNumber)
            
            plan = randomAlgorithm(plan)
            
            self.plans.append(plan)