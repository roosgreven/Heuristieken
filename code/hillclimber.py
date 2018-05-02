"""
1 May 2018.

Will contain a hill climbing algorithm.  Will first run the random algorithm
and with the solution, will start making random adjustments and only saving
those that are improvements.
"""

# Runs standard random placement algorithm
for i in range(1):
    plan = randomAlgorithm(20)
