# -*- coding: utf-8 -*-
"""
Created on Fri May 25 22:52:39 2018

@author: Gebruiker
"""

import helpers.constraints as con

def handleImpossibleMove(house, plan):
    
    if not con.checkIfPossible(house, plan):
        
        vx = house.vx
        vy = house.vy
        
        house.speed(-vx, -vy)
        house.coordinates(house.x1 - 2 * vx, house.y1 - 2 * vy)
        
        if not con.checkIfPossible(house, plan):
            
            house.speed(0, 0)
            house.coordinates(house.x1 + vx, house.y1 + vy)