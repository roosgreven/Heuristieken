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
import random
import randomalgorithm.randomalgorithm
import helpers.improvements as imp

def hillClimber(plan):

    # Initiate counter
    i = 0

    for i in range(3000):

        # Get value of plan as it is now
        oldValue = plan.getValue()

        # Random number between 0 and 1, rounded to 2 decimals
        whichMove = round(random.random(), 2)

        # 50% chance that it is a coordinate change of a single house
        if whichMove <= 0.50:

            # Select random house in houses array of current plan
            index = imp.randomHouse(plan.houses)

            # Move a house in random direction with houseMove function
            imp.houseMove(plan.houses[index], plan, oldValue)

        # 25% chance that the move is a swap of two houses
        elif whichMove <= 0.75:

            # Select random house in houses array of current plan as index 1
            index1 = imp.randomHouse(plan.houses)

            # Select random house in houses array of current plan as index 2
            index2 = imp.randomHouse(plan.houses)

            # While house indexes are the same
            while(index1 == index2):

                # Call random house function for new index2
                index2 = imp.randomHouse(plan.houses)


            # Call swap function that swaps two houses
            imp.swap(plan.houses[index1], plan.houses[index2])

            # Check if swap was viable, if not, this function sets houses back
            imp.swapCheck(plan.houses[index1], plan.houses[index2], plan, oldValue)

        # 25% chance that the move is a rotation of a single house
        else:

            # Select random house in houses array of current plan
            index = imp.randomHouse(plan.houses)

            imp.rotateHouse(plan.houses[index], plan, oldValue)

    print("hillclimber succeeded")
    return plan



if __name__ == "__main__":
    plan = hillClimber(20)

    FloorPlan.showFloorplan()
