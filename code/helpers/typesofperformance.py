"""
Contains different ways to perform an algorithm, like performing it once and
making a visualisation for the outcome, or performing the algorithm a hundred
times and saving the best one.
"""

from randomalgorithm.randomalgorithm import randomAlgorithm
from greedy.greedy import greedy
from hillclimber.hillclimber import hillClimber
from classes.floorplan import FloorPlan
import helpers.improvements as imp

def saveAndShow(algorithmType, plan):
    """ Performs an algorithm of algorithmType for the correct numberOfHouses 
    and both saves and shows it. 
    """
    
    algorithm = globals()[algorithmType]
    
    # Perform the algorithm
    plan = algorithm(plan)
        
    while len(plan.houses) < plan.numberOfHouses:
            
        plan = algorithm(plan)
    
    # Save floorplan to a csv file
    plan.saveFloorplan()

    # Make visualisation
    plan.showFloorplan()
    
def showBestAndWorst(algorithmType, numberOfHouses, numberOfIterations):
    """ Performs an algorithm of algorithmType a numberOfIterations amount of 
    iterations.  Does this for the variant of numberOfHouses.  Prints the 
    average value of the plan and visualizes the best and worst plan.
    """
    
    algorithm = globals()[algorithmType]
    bestValue = 0
    worstValue = 10 ** 20
    totalValue = 0
    
    # Perform the algorithm numberOfIterations amount of times
    for i in range(numberOfIterations):
        
        plan = FloorPlan(numberOfHouses)
        
        plan = algorithm(plan)
        
        while len(plan.houses) < numberOfHouses:
            
            plan = algorithm(plan)
            
        # Save the plan if it's either the best or worst
        value = plan.getValue()
        
        if value > bestValue:
            
            bestPlan = plan
            bestValue = value
        
        if value < worstValue:
            
            worstPlan = plan
            worstValue = value
            
        totalValue += value
    
    # Output
    print("The average value was:")
    print(totalValue / numberOfIterations)
    
    print("The best plan:")
    bestPlan.showFloorplan()
    print("The worst plan:")
    worstPlan.showFloorplan()
        