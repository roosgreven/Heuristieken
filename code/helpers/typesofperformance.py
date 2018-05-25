"""
Contains different ways to perform an algorithm, like performing it once and
making a visualisation for the outcome, or performing the algorithm a hundred
times and saving the best one.
"""

from algorithms.randomalgorithm import randomAlgorithm
from algorithms.greedy import greedy
from algorithms.hillclimber import hillClimber
from algorithms.particleswarm import particleSwarm
from classes.floorplan import FloorPlan
import experiments.convertToJSON as converter
import csv
import sys

def saveAndShow(algorithmType, plan, iterations):
    """ Performs an algorithm of algorithmType on the given plan and both saves
    and shows it.

    Arg1:
        algorithmType: type of algorithm performed, string

    Arg2: 
        plan: current floorplan
    
    Arg3:
        iterations: number of iterations to perform, integer

    """

    algorithm = globals()[algorithmType]

    # Performs iterating algorithm
    if algorithmType == "hillClimber":
        
        # Show floorplan before performing algorithm
        plan.showFloorplan()

        plan = algorithm(plan, iterations)

        while(len(plan.houses) < plan.numberOfHouses):

            plan = algorithm(plan, iterations)

    # Perform constructive
    else: 
        
        plan = algorithm(plan)

        while len(plan.houses) < plan.numberOfHouses:

            plan = algorithm(plan)

    # Save floorplan to a csv file
    if sys.argv[1] == "simulatedannealing":
        plan.saveFloorplan("simulatedannealing", len(plan.houses))

    else:
        plan.saveFloorplan(algorithmType, len(plan.houses))

    # Make visualisation
    plan.showFloorplan()

def saveAndShowPopulation(algorithmType, population, iterations):
    """ Perfroms a population based algorithm of algorithmType on the given
    plan and bot saves and shows it.

    Arg1:
        algorithmType: type of algorithm performed, string.

    Arg2:
        population: population used. 

    Arg3: 
        iterations: number of iterations to perform, integer
    """

    algorithm = globals()[algorithmType]
    
    # Get gBest at start
    population.checkForPAndGBest()
    firstGBest = population.gBest

    firstGBest.showFloorplan()

    # Perform the algorithm
    population = algorithm(population, iterations)
    
    population.plans[0].showFloorplan()

    # If the algorithm found a better gbest, a visualisation is made
    if population.gBest.getValue() > firstGBest.getValue():
        
        print(population.gBest.getValue())
        print(population.firstGBest)
        
        population.gBest.saveFloorplan(algorithmType, len(population.gBest.houses))
        
        population.gBest.showFloorplan()
        
    else:
        
        print("Failed to find better floorplan.")

def experiment(algorithmType, numberOfHouses, numberOfIterations, algorithmName, iterations):
    """ Performs an algorithm of algorithmType a numberOfIterations amount of
    iterations.  Does this for the variant of numberOfHouses.  Prints the
    average value of the plan and visualizes the best and worst plan.

    Arg1:
        algorithmType: type of algorithm performed, string

    Arg2: 
        numberOfHouses: number of houses in floorplan, integer

    Arg3:
        numberOfIterations: number of iterations to perform, integer

    Arg4: 
        AlgorithmName: name of algorithm performed

    Arg5:
        iterations: iterations for hillclimber, integer

    """

    algorithm = globals()[algorithmType]

    experimentInfo = []

    # Perform the algorithm numberOfIterations amount of times
    for i in range(numberOfIterations):

        plan = FloorPlan(numberOfHouses)

        if algorithmType == "hillClimber":

            plan = randomAlgorithm(plan)

            plan = algorithm(plan, iterations)

            while len(plan.houses) < numberOfHouses:

                plan = randomAlgorithm(plan)

                plan = algorithm(plan, iterations)

        else: 

            plan = algorithm(plan)

            while len(plan.houses) < numberOfHouses:

                plan = algorithm(plan)

        # Save the plan value
        value = plan.getValue()

        plan.saveFloorplan(algorithmType, numberOfHouses)

        experimentInfo.append([i + 1, value])

        print("Iteration: ", i + 1)

    # Write all values to csv file to use for visualisation
    with open("code/experiments/" + algorithmName + "_" + str(numberOfIterations) +  "_" 
        + str(numberOfHouses) + ".csv", "w", newline = "") as myFile:
        
        writer = csv.writer(myFile)

        # Write the changed values
        writer.writerows(experimentInfo)

    converter.convert(algorithmName, numberOfIterations, numberOfHouses)