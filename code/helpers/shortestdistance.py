"""
24 April 2018.

Calculates the shortest distance between two houses. To do this, it is first
determined between which walls or whichs corners the shortest distance is
located.
"""

def shortest(house1, house2):
    
    # x coordinate 1 of house 1
    x1h1 = house1.x1
    # x 1 of house 2
    x1h2 = house2.x1
    # x 2 of house 1
    x2h1 = house1.x2
    # x 2 of house 2
    x2h2 = house2.x2

    # y 1 of house 1
    y1h1 = house1.y1
    # y 1 of house 2
    y1h2 = house2.y1
    # y 2 of house 1
    y2h1 = house1.y2
    # y 2 of house 2
    y2h2 = house2.y2
    
    # The first two if statements check if the houses are directly horizontal or
    # vertical to each other. (Or inside each other.) The other two if statements
    # can determine between which corners the shortest distance is located 
    # otherwise.

    # Checks if the houses are above each other.
    if x1h1 <= x1h2 <= x2h1 or x1h1 <= x2h2 <= x2h1 or x1h2 <= x1h1 <= x2h2 or x1h2 <= x2h1 <=x2h2:

        # Checks if the houses are next to each other.
        if y1h1 <= y1h2 <= y2h1 or y1h1 <= y2h2 <= y2h1 or y1h2 <= y1h1 <= y2h2 or y1h2 <= y2h1 <=y2h2:
            
            # If they are both above and nest to each other, they must be inside
            # each other, the total distance is returned as 0.
            return 0

        # Checks if house 2 is above of house 1.
        elif y1h1 > y2h2:
            
            # If so, the distance between the upper wall of house 1 and the lower
            # wall of house 2 is returned.
            return y1h1 - y2h2

        # Checks if house 2 is to the right of house 1
        elif y2h1 < y1h2:
            
            # If so, the distance between the lower wall of house 1 and the upper
            # wall of house 2 is returned.
            return y1h2 - y2h1

    # Checks if the houses are next to each other.
    elif y1h1 <= y1h2 <= y2h1 or y1h1 <= y2h2 <= y2h1 or y1h2 <= y1h1 <= y2h2 or y1h2 <= y2h1 <=y2h2:

        # Checks if house 2 is to the left of house 1.
        if x1h1 > x2h2:
            
            # If so, the distance between the left wall of house 1 and the right
            # wall of house 2 is returned.
            return x1h1 - x2h2

        # Checks if house 2 is to the right of house 1.
        elif x2h1 < x1h2:
            
            # If so, the distance between the right wall of house 1 and the left
            # wall of house 2 is returned.
            return x1h2 - x2h1

    # The rest of the statements checks between which corners the shortest 
    # distance is located. This distance is calculated with Pythagoras, using
    # the coordinates of the corners in question.

    # Checks if house 2 is to the left of house 1.
    elif x1h1 > x2h2:

        # Checks if house 2 is above house 1.
        if y1h1 > y2h2:
            
            # House 2 is located to the top left of house 1.
            return ((y1h1 - y2h2) ** 2 + (x1h1 - x2h2) ** 2) ** 0.5

        # Checks if house 2 is below house 1.
        elif y2h1 < y1h2:
            
            # House 2 is located to the bottom left of house 1.
            return ((y1h2 - y2h1) ** 2 + (x1h1 - x2h2) ** 2) ** 0.5

    # Checks if house 2 is to the right of house 1.
    elif x2h1 < x1h2:

        # Checks if house 2 is above house 1.
        if y1h1 > y2h2:
            
            # House 2 is located to the top right of house 1.
            return ((y1h1 - y2h2) ** 2 + (x1h2 - x2h1) ** 2) ** 0.5

        # Checks if house 2 is below house 1.
        elif y2h1 < y1h2:
            
            # House is located to the bottom right of house 1.
            return ((y1h2 - y2h1) ** 2 + (x1h2 - x2h1) ** 2) ** 0.5

    # This should never occur, but it's here as a safety net.
    else:
        print("error")
        return -1
