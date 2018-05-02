"""
24 April 2018.

Performs a random algorithm to solve Amstelhaege.  First places all the water
randomly, then places all houses randomly. It always checks if a water or house
is actually allowed to be placed at a certain coordinate befor placing it.  Still
needs a way to check if all houses were actually placed in the given number of 
iteratations and if not handle accordingly.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import random
import matplotlib.pyplot as plt
import helpers.constraints as con
import classes.water as wt
import helpers.output as output

def randomAlgorithm(houseNumber):
    """ Performs a random algorithm, first placing water, then placing houses.
    houseNumber is the number of houses that have to be in the neighbourhood.
    """

    # j checks how many times the while loop of house placement has run
    j = 0
    i = 0
    plan = FloorPlan(houseNumber)

    # Place four water ponds
    while len(plan.ponds) < 4:

        # Get random coordinates
        x, y = random_coordinates(plan)

        # Call water placement function
        water_placement(x, y, plan)

    # Loop over houses also check if while loop is not endless by using j
    while i < plan.numberOfHouses and j < 100000:

        # Get random coordinates
        x, y = random_coordinates(plan)

        randomHouse = house_placement(x, y, plan)

        # Add 1 to while loop counter
        j += 1

        # Check if there's overlap, if not, add house to array
        if con.noWaterAndBoundary(randomHouse, plan):

            distance = fch.findClosestHouse(plan.houses, randomHouse)
            
            if not distance < randomHouse.freeSpace:
                # Add placed randomly house
                plan.houses.append(randomHouse)
                i += 1

    print("Number of times iterated through loop:")
    print(j)

    return plan

def water_placement(x, y, plan):
    """ Places water at random location. x and y form the random coordinate. """    
    
    # Initiate random water pond
    waterPond = wt.Pond(x, y)

    if con.noWaterAndBoundary(waterPond, plan):

        plan.ponds.append(waterPond)

def random_coordinates(plan):
    """ Sets random coordinates x and y. """

    # Random coordinates
    x = round(random.random() * plan.width, 1)
    y = round(random.random() * plan.length, 1)
    return x, y

def house_placement(x, y, plan):
    """ Initiates new house to place at position (x,y). """
    
    # Decide what type of house will be placed
    if len(plan.houses) < plan.numberOfEengezins:
        house = hs.Eengezins(x, y)

    elif len(plan.houses) < plan.numberOfEengezins + plan.numberOfBungalows:
        house = hs.Bungalow(x, y)

    else:
        house = hs.Maison(x, y)

    return house

if __name__ == "__main__":
    plan = randomAlgorithm(60)
    
    output.Output(plan)
