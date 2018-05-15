# -*- coding: utf-8 -*-
"""
Created on Tue May 15 14:30:23 2018

Contains functions for the improvements made in hillclimber.  Possibilities:
swap two houses, rotate a house, move a house.
"""

def swap(house1, house2):
    """ Swaps the lower left coordinates of two houses. """
    
    tempX = house2.x1
    tempY = house2.y1
    
    house2.coordinates(house1.x1, house1.y1)
    house1.coordinates(tempX, tempY)