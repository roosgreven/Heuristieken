import helpers.constraints as con

def handleImpossibleMove(house, plan):
    """ Helper function that checks if a house is within the constraints. If
        not, it finds a place where the house can stand.

        Args: 
            house: the house that has to be within the constraints. 
            plan: the floorplan that the house is in. """
    
    if not con.checkIfPossible(house, plan):
        
        vx = house.vx
        vy = house.vy
        
        house.speed(-vx, -vy)
        house.coordinates(house.x1 - 2 * vx, house.y1 - 2 * vy)
        
        if not con.checkIfPossible(house, plan):
            
            house.speed(0, 0)
            house.coordinates(house.x1 + vx, house.y1 + vy)