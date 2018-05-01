"""
27 April 2018

Runs the algorithms to solve Amstelhaege
"""

from randomalgorithm import randomAlgorithm
from greedy import greedy
import helpers.output as output
import csv
import sys

def main():

    # If not enough command arguments were provided
    if len(sys.argv) != 3:
        print("Error: usage of program should be: filename function numberOfHouses")
        exit(1)

    if int(sys.argv[2]) == 20 or int(sys.argv[2]) == 40 or int(sys.argv[2]) == 60:

        # Runs standard random placement algorithm
        for i in range(1):

            # Number of houses is third argument of command line
            houses = int(sys.argv[2])

            # Function is second argument, for instance randomAlgorithm
            # eval idea was retrieved from https://stackoverflow.com/questions/29854353/use-python-command-line-argument-as-function-names-and-function-values
            # eval was needed to turn the argv[1] into a callable function
            plan = eval(sys.argv[1])(houses)

        # Output plan
        output.Output(plan)

        # Initialize empty list
        coordinates = []

        # Add header rows to csv file
        coordinates.append(["Type", "x1", "x2", "y1", "y2"])

        # Iterate over ponds array of plan
        for pond in plan.ponds:

            # Append coordinates of each pond to coordinates array
            coordinates.append(["Water", pond.x1, pond.x2, pond.y1, pond.y2])

        totalValue = 0

        # Iterate over houses array in plan
        for house in plan.houses:

            # Add value of each house to totalValue
            totalValue += house.value(plan.houses)

            # Append coordinates of each house to coordinates array
            coordinates.append(["House",house.x1, house.x2, house.y1, house.y2])

        # Append total value to coordinates list
        coordinates.append(["totalValue", totalValue])

        # Retrieved from https://code.tutsplus.com/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907
        myFile = open('houseplan.csv', 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(coordinates)

    # If number of houses given in argument line is not valid
    else:
        print("Error: number of houses has to be 20, 40 or 60")
        exit(1)

if __name__ == "__main__":
    main()
