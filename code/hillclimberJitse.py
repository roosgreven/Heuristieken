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
from randomalgorithm import housePlacement

def hillClimber(houseNumber, plan):

    # FUNCTIES IN FLOORPLAN BEKIJKEN en MOVEMENT HUIS MET OUDE PLAN DOEN. DIT MOET OMDAT ALS JE HET HUIS
    # EERST NAAR RECHTS VERPLAATS, JE DEZE WEER OP DE OUDE POSITIE ZET ALS JE HET HUIS NAAR LINKS VERPLAATS.
    # IPV VERWIJDEREN HUIS EN OPNIEUW PLAATSEN, ALLEEN COORDINATEN AANPASSEN
    # VERGELIJKEN MET OUDE PLAN, KLEINER OF GELIJK AAN ZODAT JE NIET IN LOKAAL VAST KOMT TE ZITTEN
    # GEEN HOUSE NUMBER DOORGEVEN OMDAT PLAN AL WEET HOEVEEL HUIZEN HET ZIJN
    # IPV LINKS RECHT ONDER BOVEN, DE COORDINAAT VERANDERING DOORGEVEN
    # 1 MOVE PER HUIS EN DAN NAAR VOLGEND HUIS IN RANDOM DIRECTION
    #

    # ANDERE ALGORITMEN:
    # GENETISCHE ALGORITMEN
    # POPULATION ALGORITMEN
    

    # Safe old plan
    # OPLETTEN MET POINTERS, COPY MODULE
    oldPlan = plan

    # First initiate new plan to old plan
    newPlan = oldPlan

    # Initiate counters
    i = 0

    # Calculate value of old plan
    value_old_plan = totalValueCalculator(oldPlan)

    # Initiate index
    index = 0

    for i in range(50):

        # Select random house in houses array of current plan
        index = random_house(newPlan.houses)

        # Move house to right
        house_move(newPlan.houses[index], "right")

        # Calculate new value of plan after movement
        value_new_plan_right = total_value_calculator(newPlan)

        # Use len(newPlan.houses) - 1, because the last house was appended at the end of array
        house_move(newPlan.houses[len(newPlan.houses)-1], "left")

        # Calculate new value of plan after movement
        value_new_plan_left = total_value_calculator(newPlan)

        # If move to left returns better value than to the right
        if value_new_plan_left > value_new_plan_right:
            best_move = "left"
        else:
            best_move = "right"

        # Move house upwards
        house_move(newPlan.houses[len(newPlan.houses)-1], "upwards")

        # Calculate new value of plan after movement
        value_new_plan_upwards = total_value_calculator(newPlan)

        # If move to left returns better value than to the right
        if best_move == "right":
            if value_new_plan_upwards > value_new_plan_right:
                best_move = "upwards"

        else:
            if value_new_plan_upwards > value_new_plan_left:
                best_move = "upwards"

        # Move house downwards
        house_move(newPlan.houses[len(newPlan.houses)-1], "downwards")

        # Calculate new value of plan after movement
        value_new_plan_downwards = total_value_calculator(newPlan)

        if value_new_plan_downwards > best_move:
            best_move = "downwards"

        # Use best move and add it to newplan
        house_move(newPlan.houses[len(newPlan.houses)-1], best_move)

        # Calculate value new plan using the best move
        value_new_plan = total_value_calculator(newPlan)

        if value_new_plan > value_old_plan:
            # If the new plan is better, save it
            Oldplan = Newplan

        else:
            # If the new plan is worse, go back to old plan
            Newplan = Oldplan

    return newPlan

def total_value_calculator(plan):
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

def house_move(houseToBeMoved, direction):
    """ Moves a house in a random direction with using a distance between 0.0 and 1.0
        This function only runs 10 times (using j counter).
        If after the 10th time a good move is still not found,the random_move stops."""

    # Save current coordinates
    x1 = houseToBeMoved.x1
    y1 = houseToBeMoved.y1

    movement = 0.5


    # Remove house
    del houseToBeMoved

    if direction == "right":
        # Move house 0.5m to right
        newx1 = x1 + 0.5

        # Places house using house_placement function from randomAlgorithm,
        # returns a house at new x and old y coordinates
        house_placement(newx1, y1, newPlan)

    elif direction == "left":
        # Move house 0.5m to left
        newx1 = x1 - 2 * movement

        # Places house using house_placement function from randomAlgorithm,
        # returns a house at new x and old y coordinates
        house_placement(newx1, y1, newPlan)

    elif direction == "upwards":
        # Move house 0.5m upwards
        newy1 = y1 + 0.5

        # Set house at the old x coordinate
        newx1 = x1 + movement

        # Places house using house_placement function from randomAlgorithm,
        # returns a house at old x and new y coordinates
        house_placement(newx1, newy1, newPlan)

    elif direction == "downwards":

        # Move house 0.5m downwards
        newy1 = y1 - movement

        # Places house using house_placement function from randomAlgorithm,
        # returns a house at new x and y coordinates
        house_placement(x1, newy1, newPlan)

    else:
        return 1

    # Check if there's overlap, if not, add house to array
    if con.noWaterAndBoundary(house, newPlan):

        distance = fch.findClosestHouse(newPlan.houses, house)

        if not distance < house.freeSpace:

            # Add placed house
            newPlan.houses.append(house)
    else:

        # Stop moving this house
        return 1

if __name__ == "__main__":
    plan = hillClimber(20)

    output.Output(plan)
