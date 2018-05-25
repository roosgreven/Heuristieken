"""
25 May 2018.

Will contain a hill climbing algorithm.  Will first run the random algorithm
and with the solution, will start making random adjustments and only saving
those that are improvements.
"""

import random
import helpers.improvements as imp
import sys

def hillClimber(plan, iterations):
    """ Hillclimber function that will increase the value of the given plan step
        by step. Selects a random house and either rotates the house, swaps the 
        house with another or moves the house. Checks whether this is a viable option 
        and whether the value of the plan has increased. If so, the move updates the 
        plan. 

        Args: 
            plan: floorplan with the correct number of houses. 
            The second argument, simulatedAnnealing, can
        also be entered by the user. If this is the case, the hillclimber
        function will also accept a decrease in value of the plan with a certain
        probability. """

    print(iterations)

    # initiate simulatedAnnealing boolean
    simulatedAnnealing = True

    if sys.argv[1] == "simulatedannealing" or sys.argv[1] == "simulatedannealingExperiment":
        simulatedAnnealing = True
        temp = 50000.
    else:
        simulatedAnnealing = False
        temp = 0.

    # Initiate cooling rate for simulated annealing
    coolingRate = 0.95

    for i in range(iterations):

        # Get value of plan as it is now
        oldValue = plan.getValue()

        # Random number between 0 and 1, rounded to 2 decimals
        whichMove = round(random.random(), 2)

        # 50% chance that it is a coordinate change of a single house
        if whichMove <= 0.6:

            # Select random house in houses array of current plan
            index = imp.randomHouse(plan.houses)

            # Move a house in random direction with houseMove function
            imp.houseMove(plan.houses[index], plan, oldValue, temp)

            # Decrease temperature in case of simulated annealing
            if simulatedAnnealing == True:
               
                temp *= coolingRate

        # 25% chance that the move is a swap of two houses
        elif whichMove <= 0.8:

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
            imp.swapCheck(plan.houses[index1], plan.houses[index2], plan, oldValue, temp)
 
            # Decrease temperature in case of simulated annealing
            if simulatedAnnealing == True:
               
                temp *= coolingRate

        # 25% chance that the move is a rotation of a single house
        else:

            # Select random house in houses array of current plan
            index = imp.randomHouse(plan.houses)

            # Rotate house if possible
            imp.rotateHouse(plan.houses[index], plan, oldValue, temp)
            
            # Decrease temperature in case of simulated annealing
            if simulatedAnnealing == True:
               
                temp *= coolingRate

    return plan
