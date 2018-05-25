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
import sys

def hillClimber(plan):
    """ Hillclimber function that will increase the value of the given plan step
        by step. It starts off by selecting a random house and then it will
        either rotate the house, swap the house with another or move the house.
        After this, the function checks whether this is a viable option and
        whether the value of the plan has increased. If this is all true, then
        the move updates the plan. The second argument, simulatedAnnealing, can
        also be entered by the user. If this is the case, the hillclimber
        function will also accept a decrease in value of the plan with a certain
        probability. """

    iterations = 3000

    # initiate simulatedAnnealing boolean
    simulatedAnnealing = True

    if sys.argv[1] == "simulatedannealing" or sys.argv[1] == "simulatedannealingExperiment":
        simulatedAnnealing = True
    else:
        simulatedAnnealing = False

    # Initiate temperature for simulated annealing
    temp = 50000.

    # Initiate cooling rate for simulated annealing
    coolingRate = 0.95

    for i in range(iterations):

        # Get value of plan as it is now
        oldValue = plan.getValue()

        # Random number between 0 and 1, rounded to 2 decimals
        whichMove = round(random.random(), 2)

        # 50% chance that it is a coordinate change of a single house
        if whichMove <= 1:

            # Select random house in houses array of current plan
            index = imp.randomHouse(plan.houses)

            # Move a house in random direction with houseMove function
            if imp.houseMove(plan.houses[index], plan, oldValue, simulatedAnnealing, temp) == "Decrease Accepted":

                # Decrease temperature
                temp *= coolingRate

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
            if imp.swapCheck(plan.houses[index1], plan.houses[index2], plan, oldValue, simulatedAnnealing, temp) == "Decrease Accepted":

                # Decrease temperature
                temp *= coolingRate

        # 25% chance that the move is a rotation of a single house
        else:

            # Select random house in houses array of current plan
            index = imp.randomHouse(plan.houses)

            if imp.rotateHouse(plan.houses[index], plan, oldValue, simulatedAnnealing, temp) == "Decrease Accepted":

                # Decrease temperature
                temp *= coolingRate

    print("hillclimber succeeded")
    return plan



if __name__ == "__main__":
    plan = hillClimber(20)

    FloorPlan.showFloorplan()
