# -*- coding: utf-8 -*-
"""
Created on 15 May 2018

Contains a class with floorplans in it.
"""

from algorithms.randomalgorithm import randomAlgorithm
from classes.floorplan import FloorPlan
import copy
import matplotlib.pyplot as plt
import random
import helpers.swarmhelper as sh

class Population:
    """ Has a list (a population) of floorplans. """
    
    def __init__(self, planNumber, houseNumber, c1, c2):
        
        self.planNumber = planNumber
        self.c1 = c1
        self.c2 = c2
        
        self.plans = []
        
        self.gBest = FloorPlan(houseNumber)
        
    def makeRandomPopulation(self, houseNumber):
        """ Fills the floorplans using the random algorithm. 

            Arg1:
                houseNumber: number of houses.

        """
        
        for i in range(self.planNumber):
            
            plan = FloorPlan(houseNumber)
            
            plan = randomAlgorithm(plan)
            
            self.plans.append(plan)
            
    def checkForPAndGBest(self):
        """ Check if the current population contains a new best floorplan and
        saves it if it does. 

        """
        
        gBestValue = self.gBest.getValue()
        
        for plan in self.plans:
            
            theValue = plan.getValue()
            
            if theValue >= plan.pBestValue:
                
                if plan.checkWaterAndBoundary():
                    
                    plan.changeBest()
                    plan.pBestValue = theValue
            
            if theValue >= gBestValue:
                
                if plan.checkWaterAndBoundary():
                    
                    self.gBest = copy.deepcopy(plan)
                
                    gBestValue = theValue
                    
    def updatePopulation(self):
        """ Updates each plan in a population. """
        
        # Each plan is updated
        for plan in self.plans:
            
            # Each house is updated
            for j in range(plan.numberOfHouses):
                    
                house = plan.houses[j]
                    
                bestHouse = self.gBest.houses[j]
                    
                # The new speed is determined for each house
                vx = house.vx + self.c1 * random.random() * (house.xBest - house.x1) + self.c2 * random.random() * (bestHouse.x1 - house.x1)
                    
                vy = house.vy + self.c1 * random.random() * (house.yBest - house.y1) + self.c2 * random.random() * (bestHouse.y1 - house.y1)
                        
                # The speed is added and the coordinates updated
                house.speed(vx, vy)
                house.coordinates(house.x1 + vx, house.y1 + vy)
                    
                # Check if the house still follows the constraints
                sh.handleImpossibleMove(house, plan)
            