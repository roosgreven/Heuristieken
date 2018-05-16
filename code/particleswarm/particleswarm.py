# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:35:11 2018

Performs a particle swarm algorithm.  There's multiple floorplans, each house
of each floorplan has a speed that depends on the overall best value and the
floorplans personal best value.  The speed is used to update the population
and direct it to the best possible solution.
"""

def particleSwarm(population):
    """ Performs the algorithm. """
    
    # The current overall best is established
    population.checkForGBest()