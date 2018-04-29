"""
29 April 2018.

Contains a greedy algorithm to solve Amstelhaege. It generates a list with all
possible coordinates a house can have and iterates through this list for every
house to find the highest value place. But, whenever a house gets placed, this
reduces the number of places the next house has. The coordinates that are
impossible then get removed form the list.
"""

import classes.houses as hs
from classes.floorplan import FloorPlan
import helpers.findclosesthouse as fch
import matplotlib.pyplot as plt
import helpers.constraints as con
import classes.water as wt
import helpers.output as output

def greedy(houseNumber):
    
    plan = FloorPlan(houseNumber)
    
    plan.createCoordinates()
    
    # Places the houses with a greedy algorithm
    for i in range(houseNumber):
        
        # Decide what type of house will be placed. A testhouse is also made to
        # check for each coordinate if it's better than the current one. If it is,
        # the better coordinate will be saved.
        if i < plan.numberOfMaisons:
            
            house = hs.Maison(0, 0)
            testHouse = hs.Maison(0, 0)
            plan.currentMaisons += 1

        elif i < plan.numberOfEengezins + plan.numberOfBungalows:
            
            house = hs.Bungalow(0, 0)
            testHouse = hs.Bungalow(0, 0)
            plan.currentBungalows += 1
            
        else:
            
            house = hs.Eengezins(0, 0)
            testHouse = hs.Eengezins(0, 0)
            plan.currentEengezins += 1
            
        plan.houses.append(house)    
            
        distance = 0
        
        # Looks for the best coordinate to place a house.
        for coordinate in plan.coordinates:
            
                x, y = coordinate[0], coordinate[1]
                
                # The testhouse is set to new coordinate.
                testHouse.coordinates(x, y)
                
                # The testhouse is used to check if the house can be placed in this place.
                if con.noOverlap(plan.houses, testHouse, plan.ponds) and con.checkBoundaries(plan, testHouse):
                    
                    # The closest distance to another house are found for these
                    # coordinates.
                    newDistance = fch.findClosestHouse(plan.houses, testHouse)
                    
                    # If this distance is larger than the previous best distance,
                    # the house takes over the coordinates from the testhouse.
                    if distance < newDistance:
                        
                        distance = newDistance
                        house.coordinates(x, y)
                        
        # All coordinates that have guaranteed become unavailable because of the
        # house that was just placed, are removed from the list of coordinates.
        for x in range(int(house.x1 - house.freeSpace - plan.eengezinsWidth + 1), int(house.x2 + house.freeSpace)):
            for y in range(int(house.y1 - house.freeSpace - plan.eengezinsLength + 1), int(house.y2 + house.freeSpace)):
                
                if [x,y] in plan.coordinates:
                    plan.coordinates.remove([x,y])
            
    output.Output(plan)   
    
if __name__ == "__main__":
    greedy(20)