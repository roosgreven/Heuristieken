# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:29:16 2018

Contains a class with floorplans in it.
"""

from algorithms.randomalgorithm import randomAlgorithm
from classes.floorplan import FloorPlan
import copy
import matplotlib.pyplot as plt

class Population:
    """ Has a list (a population) of floorplans. """
    
    def __init__(self, planNumber, houseNumber):
        
        self.planNumber = planNumber
        
        self.plans = []
        
        self.gBest = FloorPlan(houseNumber)
        self.firstGBest = 0
        
    def makeRandomPopulation(self, houseNumber):
        """ Fills the floorplans using the random algorithm. """
        
        for i in range(self.planNumber):
            
            plan = FloorPlan(houseNumber)
            
            plan = randomAlgorithm(plan)
            
            self.plans.append(plan)
            
    def checkForPAndGBest(self):
        """ Check if the current population contains a new best floorplan and
        saves it if it does. """
        
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
                