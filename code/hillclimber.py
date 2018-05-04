"""
1 May 2018.

Will contain a hill climbing algorithm.  Will first run the random algorithm
and with the solution, will start making random adjustments and only saving
those that are improvements.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import helpers.constraints as con
import classes.water as wt
import helpers.output as output
import random
from randomalgorithm import randomAlgorithm
from randomalgorithm import house_placement

def hillClimber(houseNumber):

    # Initial floorplan is random
    plan = randomAlgorithm(houseNumber)

    # Safe old plan
    oldPlan = plan

    # First initiate new plan to old plan
    newPlan = oldPlan

    # Initiate counters
    i = 0

    # Calculate value of old plan
    valueOldPlan = totalValueCalculator(oldPlan)

    # Initiate index
    index = 0

    while (i < 10):

        i += 1
        j = 0

        # Select random house in houses array of current plan
        index = random_house(newPlan.houses)

        # Random move of indexed house
        random_move(newPlan.houses[index])

        # Calculate new value of plan after movement
        valueNewPlan = totalValueCalculator(newPlan)

        if valueNewPlan > valueOldPlan:
            # If the new plan is better, save it
            Oldplan = Newplan
        else:
            # If the new plan is worse, go back to old plan
            Newplan = Oldplan

    return newPlan

def totalValueCalculator(plan):
    """ Returns total value of plan """
    # Initiate total value
    totalValue = 0
    for house in plan.houses:

        totalValue += house.value(plan.houses)


def random_house(houseArray):
    """ Returns index of random house from house array in floorplan """

    # Random index of given houseArray
    index = round(random.random() * len(houseArray), 1)
    return int(index)

def random_move(houseToBeMoved):
    """ Moves a house in a random direction with using a distance between 0.0 and 1.0
        This function only runs 10 times (using j counter).
        If after the 10th time a good move is still not found,the random_move stops."""
    j += 1

    # Save current coordinates
    x1 = houseToBeMoved.x1
    y1 = houseToBeMoved.y1

    # Remove house
    del houseToBeMoved

    # Returns random number between 0.0 and 1.0
    direction = random.random()

    if direction <= 0.50:
        # New x coordinate is old x1 + random number
        newx1 = x1 + random.random()

    else:
        # New y1 coordinate is old y1 + random number
        newy1 = y1 + random.random()

    # Places house using house_placement function from randomAlgorithm,
    # returns a house at new x and y coordinates
    house_placement(newx1, newy1, newPlan)

    # Check if there's overlap, if not, add house to array
    if con.noWaterAndBoundary(house, newPlan):

        distance = fch.findClosestHouse(newPlan.houses, house)

        if not distance < house.freeSpace:

            # Add placed house
            newPlan.houses.append(house)
    else:
        if j < 10:
            # Retry random move if counter is below 10
            random_move(houseToBeMoved)
        else:
            # Stop moving this house
            return 1

if __name__ == "__main__":
    plan = hillClimber(20)

    output.Output(plan)
