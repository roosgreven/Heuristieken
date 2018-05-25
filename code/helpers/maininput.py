
"""
Checks if system arguments were correct.
"""

import sys

def sysArguments():

	if sys.argv[1] != "hillclimber" or sys.argv[1] != "simulatedannealing" or sys.argv[1] != "particleswarm":
	    
	    # If not enough command arguments were provided
	    if len(sys.argv) != 3:
	        print("Error: usage of program should be: filename function numberOfHouses")
	        exit(1)
	else: 
		if len(sys.argv) != 4:
			print("Error: usage of program should be: filenamefunction numberOfHouses [iterations]")

	# If number of houses provided was incorrect
	if not (int(sys.argv[2]) == 20 or int(sys.argv[2]) == 40 or int(sys.argv[2]) == 60):
	    print("Error: number of houses has to be 20, 40 or 60")
	    exit(1)
