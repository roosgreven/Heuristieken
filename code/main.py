"""
27 April 2018

Runs the algorithms to solve Amstelhaege.  
"""

from algorithms.randomalgorithm import randomAlgorithm
import helpers.maininput as maininput
import sys
import helpers.typesofperformance as top
from classes.floorplan import FloorPlan
from classes.population import Population

def main():
    """ Performs desired algorithm for desired number of houses, handles output
    and saves best outcome.
    """
    # Check if user input was correct
    maininput.sysArguments()

    # Number of houses is third argument of command line
    numberOfHouses = int(sys.argv[2])

    # argv[1] will decide what algorithm will be run in what way, usage of
    # argv[1] is included in the README

    # Run greedy, save and show result
    if sys.argv[1] == "greedy":

        plan = FloorPlan(numberOfHouses)

        top.saveAndShow("greedy", plan)

    # Run random, save and show result
    elif sys.argv[1] == "random":

        plan = FloorPlan(numberOfHouses)

        top.saveAndShow("randomAlgorithm", plan)

    # Run hill climber, save and show result
    elif sys.argv[1] == "hillclimber":

        plan = FloorPlan(numberOfHouses)

        plan = randomAlgorithm(plan)

        # False stands for no simulated annealing
        top.saveAndShow("hillClimber", plan)

    # Run hill climber, save and show result
    elif sys.argv[1] == "simulatedannealing":

        plan = FloorPlan(numberOfHouses)

        plan = randomAlgorithm(plan)

        # False stands for no simulated annealing
        top.saveAndShow("hillClimber", plan)

    # Run particle swarm, save and show result
    elif sys.argv[1] == "particleswarm":

        planNumber = 100

        population = Population(planNumber, numberOfHouses)

        population.makeRandomPopulation(numberOfHouses)

        top.saveAndShowPopulation("particleSwarm", population)

    # Run experiment with random, so perform algorithm 5000 times and save in csv
    elif sys.argv[1] == "randomExperiment":

        numberOfIterations = 5000
        top.experiment("randomAlgorithm", numberOfHouses, numberOfIterations, "randomAlgorithm")

    elif sys.argv[1] == "greedyExperiment":

        numberOfIterations = 500

        top.experiment("greedy", numberOfHouses, numberOfIterations, "greedy")

    elif sys.argv[1] == "hillclimberExperiment":

        numberOfIterations = 100

        top.experiment("hillClimber", numberOfHouses, numberOfIterations, "hillClimber")

    elif sys.argv[1] == "simulatedannealingExperiment":

        numberOfIterations = 100

        top.experiment("hillClimber", numberOfHouses, numberOfIterations, "simulatedannealing")
    
    else:
        
        print("Error: unknown function: refer to README for accepted functions")

if __name__ == "__main__":
    main()
