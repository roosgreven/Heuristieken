# -*- coding: utf-8 -*-
"""
Created on Fri May 25 22:52:39 2018

@author: Gebruiker
"""

import helpers.constraints as con

def handleImpossibleMove(house, plan):
    
    if not con.checkIfPossible(house, plan):
        
        house.coordinates(house.x1 - house.vx, house.y1 - house.vy)