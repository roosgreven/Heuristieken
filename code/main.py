"""
27 April 2018

Runs the algorithms to solve Amstelhaege
"""

from randomalgorithm import randomAlgorithm
from greedy import greedy
import helpers.output as output

def main():

    # Runs standard random placement algorithm
    for i in range(1):
        plan = randomAlgorithm(60)

    output.Output(plan)

if __name__ == "__main__":
    main()
