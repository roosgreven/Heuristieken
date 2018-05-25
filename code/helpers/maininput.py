
"""
Checks if system arguments were correct.

Calls:
	main, if system arguments are correct.
"""

import sys

def sysArguments():
	    
    # If not enough command arguments were provided
	if len(sys.argv) != 3:
    if len(sys.argv) != 3:
		
<<<<<<< HEAD
		if sys.argv[1] != "hillclimber" and sys.argv[1] != "simulatedannealing" and sys.argv[1] != "particleswarm" and sys.argv[1] != "hillclimberExperiment" and sys.argv[1] != "simulatedannealingExperiment":
			print("Error: usage of program should be: filename function numberOfHouses")
=======
        if sys.argv[1] != "hillclimber" and sys.argv[1] != "simulatedannealing" and sys.argv[1] != "particleswarm":
            print("Error: usage of program should be: filename function numberOfHouses")
>>>>>>> 712e3686d62a8571b7fc4649bf5836af4d9f7613

			exit(1)
            exit(1)
            
        elif len(sys.argv) != 4:
            print("Error: usage of program should be: filenamefunction numberOfHouses [iterations]")
            exit(1)
            
    if len(sys.argv) == 3:
		
        if sys.argv[1] != "random" and sys.argv[1] != "greedy":
            print("Error: usage of program should be: filename function numberOfHouses [iterations]")

	else: 
		if len(sys.argv) != 4:
			print("Error: usage of program should be: filenamefunction numberOfHouses [iterations]")
			exit(1)
            exit(1)

	# If number of houses provided was incorrect
	if not (int(sys.argv[2]) == 20 or int(sys.argv[2]) == 40 or int(sys.argv[2]) == 60):
	    print("Error: number of houses has to be 20, 40 or 60")
	    exit(1)
    # If number of houses provided was incorrect
    if not (int(sys.argv[2]) == 20 or int(sys.argv[2]) == 40 or int(sys.argv[2]) == 60):
        print("Error: number of houses has to be 20, 40 or 60")
        exit(1)
