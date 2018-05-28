"""
Converts a csv file to a JSON file
"""

import csv
import json
import sys


def main():
	""" Converts csv file to JSON file. Takes in algorithm type, number of iterations
	and number of houses, to create the correct name. Finally writes the needed file.
	"""
	sys.argv[1] = 
	hillclimber = []
	simannealing = []

	numberOfHouses = 40
	counter = 0
	data = []

	with open(str(numberOfHouses) + '_iterations' + '.csv', newline = '') as csvfile:
	    thisfile = csv.reader(csvfile, delimiter = ';')
	    
	    for row in thisfile:
	        iteration = counter + counter * 9
	        data.append({"iteration": iteration , "Hillclimber": float(row[0]), "Simulated Annealing": float(row[1])})
	        counter += 1
	        
	with open(str(numberOfHouses) + '_iterations' + '.json', 'w') as outfile:
	    json.dump(data, outfile)


if __name__ == "__main__":
    main()
