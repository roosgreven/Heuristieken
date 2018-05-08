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
import random
from randomalgorithm.randomalgorithm import randomAlgorithm

def hillClimber(houseNumber, plan):

    # Safe old plan
    oldPlan = plan

    # First initiate new plan to old plan
    newPlan = oldPlan

    # Initiate counters
    i = 0

    # Calculate value of old plan
<<<<<<< HEAD:code/hillclimber.py
    value_old_plan = totalValueCalculator(oldPlan)
=======
    valueOldPlan = oldPlan.getValue()
>>>>>>> 7b0ecb8fa24e6329069cb5e4e1b6b38c42f6a6df:code/hillclimber/hillclimber.py

    # Initiate index
    index = 0

    for i in range(50):

        # Select random house in houses array of current plan
        index = randomHouse(newPlan.houses)

<<<<<<< HEAD:code/hillclimber.py
        # Move house to right
        house_move(newPlan.houses[index], right)

        # Calculate new value of plan after movement
        value_new_plan_right = total_value_calculator(newPlan)

        # Use len(newPlan.houses) - 1, because the last house was appended at the end of array
        house_move(newPlan.houses[len(newPlan.houses)-1], left)

        # Calculate new value of plan after movement
        value_new_plan_left = total_value_calculator(newPlan)

        # If move to left returns better value than to the right
        if value_new_plan_left > value_new_plan_right:
            best_move = left
        else:
            best_move = right

        # Move house upwards
        house_move(newPlan.houses[len(newPlan.houses)-1], upwards)

        # Calculate new value of plan after movement
        value_new_plan_upwards = total_value_calculator(newPlan)

        # If move to left returns better value than to the right
        if best_move == right:
            if value_new_plan_upwards > value_new_plan_right:
                best_move = upwards

        else:
            if value_new_plan_upwards > value_new_plan_left:
                best_move = upwards

        # Move house downwards
        house_move(newPlan.houses[len(newPlan.houses)-1], downwards)

        # Calculate new value of plan after movement
        value_new_plan_downwards = total_value_calculator(newPlan)

        if value_new_plan_downwards > best_move:
            best_move = downwards

        # Use best move and add it to newplan
        house_move(newPlan.houses[len(newPlan.houses)-1], best_move)
=======
        # Random move of indexed house
        randomMove(newPlan.houses[index])

        # Calculate new value of plan after movement
        valueNewPlan = newPlan.getValue()
>>>>>>> 7b0ecb8fa24e6329069cb5e4e1b6b38c42f6a6df:code/hillclimber/hillclimber.py

        # Calculate value new plan using the best move
        value_new_plan = total_value_calculator(newPlan)

        if value_new_plan > value_old_plan:
            # If the new plan is better, save it
            Oldplan = Newplan
        else:
            # If the new plan is worse, go back to old plan
            Newplan = Oldplan

    return newPlan

<<<<<<< HEAD:code/hillclimber.py
def total_value_calculator(plan):
    """ Returns total value of plan """
    # Initiate total value
    totalValue = 0
    for house in plan.houses:

        totalValue += house.value(plan.houses)

=======
>>>>>>> 7b0ecb8fa24e6329069cb5e4e1b6b38c42f6a6df:code/hillclimber/hillclimber.py

def randomHouse(houseArray):
    """ Returns index of random house from house array in floorplan """

    # Random index of given houseArray
    index = round(random.random() * len(houseArray), 1)
    return int(index)

<<<<<<< HEAD:code/hillclimber.py
def house_move(houseToBeMoved, direction):
    """ Moves a house in a random direction with using a distance between 0.0 and 1.0
        This function only runs 10 times (using j counter).
        If after the 10th time a good move is still not found,the random_move stops."""
=======
def randomMove(houseToBeMoved):
    """ Moves a house in a random direction with using a distance between 0.0 and 1.0
        This function only runs 10 times (using j counter).
        If after the 10th time a good move is still not found,the randomMove stops."""
    j += 1
>>>>>>> 7b0ecb8fa24e6329069cb5e4e1b6b38c42f6a6df:code/hillclimber/hillclimber.py

    # Save current coordinates
    x1 = houseToBeMoved.x1
    y1 = houseToBeMoved.y1

    # Remove house
    del houseToBeMoved

    if direction == right:
        # Move house 0.5m to right
        newx1 = x1 + 0.5

        # Places house using house_placement function from randomAlgorithm,
        # returns a house at new x and old y coordinates
        house_placement(newx1, y1, newPlan)

    elif direction == left:
        # Move house 0.5m to left
        newx1 = x1 - 0.5

        # Places house using house_placement function from randomAlgorithm,
        # returns a house at new x and old y coordinates
        house_placement(newx1, y1, newPlan)

<<<<<<< HEAD:code/hillclimber.py
    elif direction == upwards:
        # Move house 0.5m upwards
        newy1 = y1 + 0.5

        # Places house using house_placement function from randomAlgorithm,
        # returns a house at old x and new y coordinates
        house_placement(x1, newy1, newPlan)

    elif direction == downwards:
        # Move house 0.5m downwards
        newy1 = y1 - 0.5
        # Places house using house_placement function from randomAlgorithm,
        # returns a house at new x and y coordinates
        house_placement(x1, newy1, newPlan)

    else:
        return 1
=======
    # Places house using makeHouse function from randomAlgorithm,
    # returns a house at new x and y coordinates
    plan.makeHouse(newx1, newy1, newPlan)
>>>>>>> 7b0ecb8fa24e6329069cb5e4e1b6b38c42f6a6df:code/hillclimber/hillclimber.py

    # Check if there's overlap, if not, add house to array
    if con.noWaterAndBoundary(house, newPlan):

        distance = fch.findClosestHouse(newPlan, house)

        if not distance < house.freeSpace:

            # Add placed house
            newPlan.houses.append(house)
    else:
<<<<<<< HEAD:code/hillclimber.py

        # Stop moving this house
        return 1
=======
        if j < 10:
            # Retry random move if counter is below 10
            randomMove(houseToBeMoved)
        else:
            # Stop moving this house
            return 1
>>>>>>> 7b0ecb8fa24e6329069cb5e4e1b6b38c42f6a6df:code/hillclimber/hillclimber.py

if __name__ == "__main__":
    plan = hillClimber(20)

    # Make visualisation
    plan.showFloorplan()