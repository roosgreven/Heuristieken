"""
Converts a csv file to a JSON file
"""

import csv
import json
import math

def convert(algorithmType, numberOfIterations, numberOfHouses):
	""" Converts csv file to JSON file. Takes in algorithm type, number of iterations
	and number of houses, to create the correct name. Finally writes the needed file.
	"""

	# Array to store data
	data = []

	# Open the CSV file to find minimum and maximum data
	with open('code/experiments/' + algorithmType + '_' + str(numberOfIterations) +  '_' 
        + str(numberOfHouses) + '.csv', newline='') as csvfile:

		# Read CSV file
		reader = csv.reader(csvfile, delimiter = ',')

	# Open the CSV file to group the data
	with open('code/experiments/' + algorithmType + '_' + str(numberOfIterations) +  '_' 
        + str(numberOfHouses) + '.csv', newline='') as csvfile:

		# Read CSV file
		reader = csv.reader(csvfile, delimiter = ',')

		if numberOfHouses == 20:

			# Decide when to start bar chart
			startChart = 7500000

			# Decide when to stop bar chart
			endChart = 11500000

		elif numberOfHouses == 40:

			startChart = 14000000
			endChart = 20500000

		else:

			startChart = 21000000
			endChart = 28000000

		# Calculate range of values
		valueRange = endChart - startChart

		# Calculate ranges of charts
		oneStep = valueRange / 20

		group1 = group2 = group3 = group4 = group5 = group6 = group7 = group8 = group9 = group10 = 0

		group11 = group12 = group13 = group14 = group15 = group15 = group16 = group17 = group18 = group19 = group20 = 0

		# Loop over all lines in file
		for row in reader:

			# Group all values in ranges
			group = math.floor((float(row[1]) - startChart) / oneStep)
			
			if group == 0:
				group1 += 1
			elif group == 1:
				group2 += 1
			elif group == 2:
				group3 += 1
			elif group == 3:
				group4 += 1
			elif group == 4:
				group5 += 1
			elif group == 5:
				group6 += 1 
			elif group == 6:
				group7 += 1
			elif group == 7:
				group8 += 1
			elif group == 8:
				group9 += 1
			elif group == 9:
				group10 += 1
			elif group == 10:
				group11 += 1
			elif group == 11:
				group12 += 1
			elif group == 12:
				group13 += 1
			elif group == 13:
				group14 += 1 
			elif group == 14:
				group15 += 1
			elif group == 15:
				group16 += 1
			elif group == 16:
				group17 += 1
			elif group == 17:
				group18 += 1
			elif group == 18:
				group19 += 1
			else:
				group20 +=1

		for i in range(1, 21):

			# Store data as dictionary in new array
			data.append({'range': '€' + str(startChart + (i - 1) * int(oneStep)) + ' - ' + '€' + str((startChart + (i * int(oneStep)))), 
				'frequency': eval("group" + str(i)) / numberOfIterations * 100 })

		# Save data in new file
		with open('code/experiments/' + algorithmType + '_' + str(numberOfIterations) +  '_' 
			+ str(numberOfHouses) + '.json', 'w') as outfile:

			# Save data as JSON
			json.dump(data, outfile)
		
		print("startchart: ", startChart, "endChart: ", endChart)

		print("value range: ", valueRange, "oneSteps: ", oneStep)