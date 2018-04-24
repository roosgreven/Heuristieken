def Shortest(house1, house2):

    x1h1 = house1.x1
    x1h2 = house2.x1
    x2h1 = house1.x2
    x2h2 = house2.x2

    y1h1 = house1.y1
    y1h2 = house2.y1
    y2h1 = house1.y2
    y2h2 = house2.y2

    if x1h1 <= x1h2 <= x2h1 or x1h1 <= x2h2 <= x2h1:

        # houses inside each other
        if y1h1 <= y1h2 <= y2h1 or y1h1 <= y2h2 <= y2h1:
            return 0

        # only vertical separation
        elif y1h1 > y2h2:
            return y1h1 - y2h2

        elif y2h1 < y1h2:
            return y1h2 - y2h1

    elif y1h1 <= y1h2 <= y2h1 or y1h1 <= y2h2 <= y2h1:

        # only horizontal separation
        if x1h1 > x2h2:
            return x1h1 - x2h2

        elif x2h1 < x1h2:
            return x1h2 - x2h1

    elif x1h1 > x2h2:

        # house2 is left above house1
        if y1h1 > y2h2:
            return ((y1h1 - y2h2) ** 2 + (x1h1 - x2h2) ** 2) ** 0.5

        # house2 is left below house1
        elif y2h1 < y1h2:
            return ((y1h2 - y2h1) ** 2 + (x1h1 - x2h2) ** 2) ** 0.5

    elif x2h1 < x1h2:

        # house2 is right above house1
        if y1h1 > y2h2:
            return ((y1h1 - y2h2) ** 2 + (x1h2 - x2h1) ** 2) ** 0.5

        # house2 is right below house1
        elif y2h1 < y1h2:
            return ((y1h2 - y2h1) ** 2 + (x1h2 - x2h1) ** 2) ** 0.5

    # error
    else:
        return -1
