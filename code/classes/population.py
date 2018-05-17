# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:29:16 2018

Contains a class with floorplans in it.
"""

from randomalgorithm.randomalgorithm import randomAlgorithm
from classes.floorplan import FloorPlan
import copy
import matplotlib.pyplot as plt

class Population:
    """ Has a list (a population) of floorplans. """
    
    def __init__(self, planNumber, houseNumber):
        
        self.planNumber = planNumber
        
        self.plans = []
        
        self.gBest = FloorPlan(houseNumber)
        
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
                
                plan.changeBest()
                plan.pBestValue = theValue
            
            if theValue >= gBestValue:
                
                if plan.checkWaterAndBoundary():
                    
                    self.gBest = copy.deepcopy(plan)
                
                    gBestValue = theValue
                
    def showPopulation(self):
        
        for plan in self.plans:
            
            # Visualisation of the floor plan
            plt.figure()

            # These coordinates together plot the outline of the neighbourhood
            xlist = [0, plan.width, plan.width, 0, 0]
            ylist = [0, 0, plan.length, plan.length, 0]
            plt.plot(xlist, ylist, 'm-')
    
            for pond in plan.ponds:
    
                # By plotting these lists, all corners will be connected by a line
                xlist = [pond.x1, pond.x2, pond.x2, pond.x1, pond.x1]
                ylist = [pond.y1, pond.y1, pond.y2, pond.y2, pond.y1]
    
                plt.plot(xlist, ylist, 'b-')
    
    
            for house in plan.houses:
    
                # By plotting these lists, all corners will be connected by a line
                xlist = [house.x1, house.x2, house.x2, house.x1, house.x1]
                ylist = [house.y1, house.y1, house.y2, house.y2, house.y1]
                
                color = 'y-'
    
                if house.theType == "Eengezins":
                    color = 'r-'
                elif house.theType == "Bungalow":
                    color = 'g-'
                elif house.theType == "Maison":
                    color = 'c-'
                    
                plt.plot(xlist, ylist, color)
                
        plt.show()
        
        
        
        