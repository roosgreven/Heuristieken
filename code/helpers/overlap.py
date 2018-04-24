"""
Returns True when overlap of houses exists
"""
def Overlap(house1, house2):

    # X coordinates of house 1 and house 2
    x1h1 = house1.x1
    x1h2 = house2.x1
    x2h1 = house1.x2
    x2h2 = house2.x2

    # Y coordinates of house 1 and house 2
    y1h1 = house1.y1
    y1h2 = house2.y1
    y2h1 = house1.y2
    y2h2 = house2.y2

    # If x coordinates of houses are in same range
    if x1h1 <= x1h2 <= x2h1 or x1h1 <= x2h2 <= x2h1:

        # Overlap
        if y1h1 <= y1h2 <= y2h1 or y1h1 <= y2h2 <= y2h1:
            return True

    # No overlap
    return False
