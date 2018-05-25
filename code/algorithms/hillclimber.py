"""
25 May 2018.
Contqains a hill climbing algorithm.  Will first run the random algorithm
and with the solution, will start making random adjustments and only saving
those that are improvements.
"""

import random
import helpers.improvements as imp
import sys

def hillClimber(plan, iterations):
    """ Increases value of the given plan stepby step. Selects a random house and either 
        rotates, swaps with another or moves the house. Checks whether this is a viable option 
        and whether the value of the plan has increased. If so, the move updates the 
        plan. Performs simulated annealing algorithm if system argument is simulated annealing. 

        Arg1: 
            plan: floorplan with the correct number of houses. 
        Arg2:
            iterations: number of iterations to perform
    """

    # Checks if the algorithm is simulated annealing or hill climber, simulated
    # annealing gets a temperature, hill climber temperature is set to zero
    if sys.argv[1] == "simulatedannealing" or sys.argv[1] == "simulatedannealingExperiment":
        temp = 50000.
        
    else:
        temp = 0.

    # Initiate cooling rate for simulated annealing
    coolingRate = 0.95

    for i in range(iterations):

        # Get value of plan as it is now
        oldValue = plan.getValue()
        
        # Select house that will undergo change
        index = imp.randomHouse(plan.houses)

        # Random number between 0 and 1, rounded to 2 decimals
        whichMove = round(random.random(), 2)

        # A house will change coordinates
        if whichMove <= 0.6:
            
            # Move a house in random direction with houseMove function
            imp.houseMove(plan.houses[index], plan, oldValue, temp)

        # Two houses will swap position
        elif whichMove <= 0.8:
            
            # Select additional house to be swapped
            index2 = imp.randomHouse(plan.houses)

            # Can't risk swapping a house with itself
            while(index == index2):

                # Call random house function for new index2
                index2 = imp.randomHouse(plan.houses)


            # Call swap function that swaps two houses
            imp.swap(plan.houses[index], plan.houses[index2])

            # Check if swap was viable, if not, this function sets houses back
            imp.swapCheck(plan.houses[index], plan.houses[index2], plan, oldValue, temp)

        # A house will be rotated 90 degrees
        else:
            
            # Rotate house if possible
            imp.rotateHouse(plan.houses[index], plan, oldValue, temp)
        
        # Decrease temperature
        temp *= coolingRate
        
    return plan
