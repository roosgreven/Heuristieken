
"""
Checks if system arguments were correct.
"""

import sys

def sysArguments():
	    
    # If not enough command arguments were provided
    if len(sys.argv) != 3:
		
        if sys.argv[1] != "hillclimber" and sys.argv[1] != "simulatedannealing" and sys.argv[1] != "particleswarm":
            print("Error: usage of program should be: filename function numberOfHouses")

            exit(1)
            
        elif len(sys.argv) != 4:
            print("Error: usage of program should be: filenamefunction numberOfHouses [iterations]")
            exit(1)
            
    if len(sys.argv) == 3:
		
        if sys.argv[1] != "random" and sys.argv[1] != "greedy":
            print("Error: usage of program should be: filename function numberOfHouses [iterations]")

            exit(1)

    # If number of houses provided was incorrect
    if not (int(sys.argv[2]) == 20 or int(sys.argv[2]) == 40 or int(sys.argv[2]) == 60):
        print("Error: number of houses has to be 20, 40 or 60")
        exit(1)
