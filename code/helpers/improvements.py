# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:30:23 2018

Contains functions for the improvements made in hillclimber.  Possibilities:
swap two houses, rotate a house, move a house.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import helpers.constraints as con
import random
import randomalgorithm.randomalgorithm

def randomHouse(houseArray):
    """ Returns index of random house from house array in floorplan """

    lengthHouseArray = len(houseArray) - 1

    # Random index of given houseArray
    index = round(random.random() * lengthHouseArray, 1)

    return int(index)

def houseMove(houseToBeMoved, plan, oldValue, simulatedAnnealing):
    """ First checks the value of the plan as it is. Then, moves a house in a
        random direction, using a distance between 0.0 and 1.0.
        The function checks whether the house move is viable.
        After the move has been made, it compares the plan value of the old
        situation and the new situation.
        The house will be moved back to its old position if the value has decreased"""

    # Save current coordinates
    oldx1 = houseToBeMoved.x1
    oldy1 = houseToBeMoved.y1

    # Retrieved from https://stackoverflow.com/questions/48122608/how-do-i-generate-random-float-and-round-it-to-1-decimal-place
    movementx = round(int(random.uniform(-1, 1) * 10)) / 10.0
    movementy = round(int(random.uniform(-1, 1) * 10)) / 10.0

    # New x and y coordinates
    newx1 = oldx1 + movementx
    newy1 = oldy1 + movementy

    # Change coordinates of house to be moved
    houseToBeMoved.coordinates(newx1, newy1)

    # Check if there's overlap with water and boundaries
    if con.noWaterAndBoundary(houseToBeMoved, plan):

        distance = fch.findClosestHouse(plan, houseToBeMoved)

        if distance > 0:

            newValue = plan.getValue()

            # If the house move has decreased plan value
            if not newValue >= oldValue:

                # Set house back at old position
                houseToBeMoved.coordinates(oldx1, oldy1)
        else:
            # Set house back at old position
            houseToBeMoved.coordinates(oldx1, oldy1)

    # If move is not viable, because of overlap
    else:

        # Set house back at old position
        houseToBeMoved.coordinates(oldx1, oldy1)

def swap(house1, house2):
    """ Swaps the lower left coordinates of two houses. """

    tempX = house2.x1
    tempY = house2.y1

    house2.coordinates(house1.x1, house1.y1)
    house1.coordinates(tempX, tempY)

def swapCheck(house1, house2, plan, oldValue, simulatedAnnealing):
    """ Checks if swap was viable for both houses and whether
        plan value was improved or the same. If not, houses are set back to
        old positions """

    # Check if there's overlap with water and boundaries for house 1
    if con.noWaterAndBoundary(house1, plan):

        distance = fch.findClosestHouse(plan, house1)

        if distance > 0:

            newValue = plan.getValue()

            # Do not accept decrease in value
            if simulatedAnnealing == False:

                # If the house move has decreased plan value
                if not newValue >= oldValue:
                    swap(house2, house1)

            elif simulatedAnnealing == True:
                # Hier moet probability acceptance formula komen voor verslechtering

        else:
            swap(house2, house1)

    # If move is not viable, because of overlap
    else:
        swap(house2, house1)


    # Check if there's overlap with water and boundaries for house 2
    if con.noWaterAndBoundary(house2, plan):

        distance = fch.findClosestHouse(plan, house2)

        if distance > 0:

            newValue = plan.getValue()

            # Do not accept decrease in values
            if simulatedAnnealing == False:

                # If the house move has decreased plan value
                if not newValue >= oldValue:
                    swap(house2, house1)

            elif simulatedAnnealing == True:
                # Hier moet probability acceptance formula komen voor verslechtering

        else:
            swap(house2, house1)

    # If move is not viable, because of overlap
    else:
        swap(house2, house1)


def rotateHouse(house, plan, oldValue, simulatedAnnealing):

    # Rotate house
    house.rotate()

    # Check if there's overlap with water and boundaries
    if con.noWaterAndBoundary(house, plan):

        distance = fch.findClosestHouse(plan, house)

        if distance > 0:

            newValue = plan.getValue()

            # Do not accept decrease in value
            if simulatedAnnealing == False:

                # If the house rotation has decreased plan value
                if not newValue >= oldValue:

                    # Rotate house back
                    house.rotate()

            # Do accept decrease in value with certain probability
            elif simulatedAnnealing == True:
                # Hier moet probability acceptance formula komen voor verslechtering

        else:
            # Rotate house back
            house.rotate()

    # If move is not viable, because of overlap
    else:
        # Rotate house back
        house.rotate()
