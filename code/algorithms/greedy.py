"""
29 April 2018.

Contains a greedy algorithm to solve Amstelhaege.  It generates a list with all
possible coordinates a house can have and iterates through this list for every
house to find the highest value place.  But, whenever a house gets placed, this
reduces the number of places the next house has.  
"""

import helpers.coordinates as co

def greedy(plan):
    """ Performs a greedy algorithm.  Places the water randomly and places each
    house in an optimal place. 
    
    Args:
        plan: empty floorplan.

    """

    # List of all possible coordinates is generated
    plan.createCoordinates()

    plan.makePonds()

    # Places the houses with a greedy algorithm
    for i in range(plan.numberOfHouses):

        # Initiate house
        bestX, bestY = 0, 0

        house = plan.makeHouse(bestX, bestY)

        # Find best coordinates for house
        bestX, bestY, distance = co.findCoordinates(plan, house)

        # House is added to array
        house.coordinates(bestX, bestY)
        if distance > 0:
            plan.houses.append(house)
        
        # In case there is nog place where the house fits
        else:
            print("Error: no solution found.")
        
            
        print("houses placed: ", len(plan.houses))

        # Coordinates that are now impossible for other houses are removed from
        # list
        co.removeCoordinates(plan, house)

    return plan
