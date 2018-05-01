"""
27 April 2018

Runs the algorithms to solve Amstelhaege
"""

from randomalgorithm import RandomAlgorithm
from greedy import greedy
import helpers.output as output

def main():

    # Runs standard random placement algorithm
    for i in range(1):
        plan = RandomAlgorithm(20)

    output.Output(plan)

if __name__ == "__main__":
    main()
