"""
27 April 2018

Runs the algorithms to solve Amstelhaege.  Every algorithm returns the Floorplan.
This functions can then generate the wanted output.  For the time being this
function will be changed for different desired outcomes, but will become fully
automated eventually.  For now the function also saves the outcome in a csv file.
"""

from randomalgorithm.randomalgorithm import randomAlgorithm
from greedy.greedy import greedy
from hillclimber.hillclimber import hillClimber
import helpers.maininput as maininput
import sys
import helpers.typesofperformance as top
from classes.floorplan import FloorPlan

def main():
    """ Performs desired algorithm for desired number of houses, handles output
    and saves best outcome.
    """
    # Check if user input was correct
    maininput.sysArguments()

    # Number of houses is third argument of command line
    numberOfHouses = int(sys.argv[2])
    """
    # Function is second argument, for instance randomAlgorithm
    # eval idea was retrieved from https://stackoverflow.com/questions/29854353/use-python-command-line-argument-as-function-names-and-function-values
    # eval was needed to turn the argv[1] into a callable function
    plan = eval(sys.argv[1])(houses)
    """

    # argv[1] will decide what algorithm will be run in what way, usage of
    # argv[1] is included in the README

    # run greedy, save and show result
    if sys.argv[1] == "greedy":

        plan = FloorPlan(numberOfHouses)

        top.saveAndShow("greedy", numberOfHouses, plan)

    # Run random, save and show result
    if sys.argv[1] == "random":

        plan = FloorPlan(numberOfHouses)

        top.saveAndShow("randomAlgorithm", numberOfHouses, plan)

    # Run hill climber, save and show result
    if sys.argv[1] == "hillclimber":

        plan = FloorPlan(numberOfHouses)

        top.saveAndShow("hillClimber", numberOfHouses, randomAlgorithm)

    # Run random a hundred times, calculate and print average value and
    # visualize best and worst floorplan
    if sys.argv[1] == "lotsOfRandom":

        numberOfIterations = 100

        top.showBestAndWorst("randomAlgorithm", numberOfHouses, "FloorPlan", numberOfIterations)


if __name__ == "__main__":
    main()
