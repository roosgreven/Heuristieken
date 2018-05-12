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

def hillClimber(houseNumber, plan):

    # Initiate counter
    i = 0

    for i in range(10):

        # Select random house in houses array of current plan
        index = randomHouse(plan.houses)

        # Move house in random direction with houseMove function
        houseMove(plan.houses[index], plan)

    print("hillclimber succeeded")
    return plan

def randomHouse(houseArray):
    """ Returns index of random house from house array in floorplan """

    # Random index of given houseArray
    index = round(random.random() * len(houseArray), 1)

    return int(index)

def houseMove(houseToBeMoved, plan):
    """ First checks the value of the plan as it is. Then, moves a house in a
        random direction, using a distance between 0.0 and 1.0.
        The function checks whether the house move is viable.
        After the move has been made, it compares the plan value of the old
        situation and the new situation.
        The house will be moved back to its old position if the value has decreased"""

    # Get value of plan as it is now
    oldValue = plan.getValue()

    # Save current coordinates
    oldx1 = houseToBeMoved.x1
    oldy1 = houseToBeMoved.y1

    # Retrieved from https://stackoverflow.com/questions/48122608/how-do-i-generate-random-float-and-round-it-to-1-decimal-place
    # Random.uniform: https://docs.python.org/3/library/random.html#random.uniform
    # Returns a number between -1 and 1, rounded to 1 decimal
    movementx = round(int(random.uniform(-1, 1) * 10)) / 10.0
    movementy = round(int(random.uniform(-1, 1) * 10)) / 10.0

    # New x and y coordinates
    newx1 = oldx1 + movementx
    newy1 = oldy1 + movementy

    # Change coordinates of house to be moved
    houseToBeMoved.coordinates(newx1, newy1)

    # Check if there's overlap
    if con.noWaterAndBoundary(houseToBeMoved, plan):

        distance = fch.findClosestHouse(plan, houseToBeMoved)

        if not distance < houseToBeMoved.freeSpace:

            newValue = plan.getValue()

            # If the house move has decreased plan value
            if not newValue >= oldValue:

                # Set house back at old position
                houseToBeMoved.coordinates(oldx1, oldy1)

            return plan

    # If move is not viable, because of overlap
    else:

        # Set house back at old position
        houseToBeMoved.coordinates(oldx1, oldy1)

        return plan

if __name__ == "__main__":
    plan = hillClimber(20)

    FloorPlan.showFloorplan()
