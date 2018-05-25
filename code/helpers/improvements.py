# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:30:23 2018

Contains functions for the improvements made in hillclimber.  Possibilities:
swap two houses, rotate a house, move a house.

The simulated annealing idea for initial temperature, cooling rate and acceptance
probability was retrieved from http://www.theprojectspot.com/tutorial-post/simulated-annealing-algorithm-for-beginners/6.
Initial temperature and cooling rate is found in hillclimber.py.
"""

import helpers.findclosesthouse as fch
import helpers.constraints as con
import random

def randomHouse(houseArray):
    """ Returns index of random house from house array in floorplan. """

    lengthHouseArray = len(houseArray) - 1

    # Random index of given houseArray
    index = round(random.random() * lengthHouseArray, 1)

    return int(index)

def checkIfAccepted(newValue, oldValue, temp):
    """ Decides if a change is accepted.  Always accepts improvements and in
    case of simulated annealing occasionally accepts. """
    
    if newValue < oldValue:
        
        if temp > 1:
            
            probability = (oldValue - newValue)/temp
            
            if probability > random.random():
                return True
            else:
                return False
        else:
            return False
    else:
        return True
    
def checkIfStay(house, plan, oldValue, temp):
    """ Checks if a house can stay at it's current position. """
    
    # Check if there's overlap with water and boundaries
    if con.checkIfPossible(house, plan):
        
        newValue = plan.getValue()
        
        # Check if move will be accepted
        if checkIfAccepted(newValue, oldValue, temp):
            
            return True
    
    # Move was not accepted
    return False

def move(house):
    """ Slightly moves a house. """
    
    # Save current coordinates
    oldx1 = house.x1
    oldy1 = house.y1

    # Retrieved from https://stackoverflow.com/questions/48122608/how-do-i-generate-random-float-and-round-it-to-1-decimal-place
    movementx = round(int(random.uniform(-1, 1) * 10)) / 10.0
    movementy = round(int(random.uniform(-1, 1) * 10)) / 10.0

    # New x and y coordinates
    newx1 = oldx1 + movementx
    newy1 = oldy1 + movementy
    
    # Change coordinates of house to be moved
    house.coordinates(newx1, newy1)
    
    return oldx1, oldy1

def houseMove(house, plan, oldValue, temp):
    """ First checks the value of the plan as it is. Then, moves a house in a
        random direction, using a distance between 0.0 and 1.0.
        The function checks whether the house move is viable.
        After the move has been made, it compares the plan value of the old
        situation and the new situation.
        The house will be moved back to its old position if the value has decreased. """
    
    # Save current coordinates
    oldx1, oldy1 = move(house)
    
    # Check if the house will stay in it's current position
    if not checkIfStay(house, plan, oldValue, temp):
        
        house.coordinates(oldx1, oldy1)
    
def swap(house1, house2):
    """ Swaps the lower left coordinates of two houses. """

    tempX = house2.x1
    tempY = house2.y1

    house2.coordinates(house1.x1, house1.y1)
    house1.coordinates(tempX, tempY)

def swapCheck(house1, house2, plan, oldValue, temp):
    """ Checks if swap was viable for both houses and whether
        plan value was improved or the same. If not, houses are set back to
        old positions. """

    # Check if the houses will stay in their current position
    if not (checkIfStay(house1, plan, oldValue, temp) and checkIfStay(house2, plan, oldValue, temp)):
        
        # Swap house back if not
        swap(house2, house1)

def rotateHouse(house, plan, oldValue, temp):
    
    # Rotate house
    house.rotate()
    
    # Check if the house will stay in it's current position
    if not checkIfStay(house, plan, oldValue, temp):
        house.rotate()