def Shortest(house1, house2):
    
    x11 = house1.x1
    x12 = house2.x1
    x21 = house1.x2
    x22 = house2.x2
    
    y11 = house1.y1
    y12 = house2.y1
    y21 = house1.y2
    y22 = house2.y2
    
    if x11 <= x12 <= x21 or x11 <= x22 <= x21:
        
        # houses inside each other
        if y11 <= y12 <= y21 or y11 <= y22 <= y21:
            return 0
            
        # only vertical separation
        elif y11 > y22:
            return y11 - y22
            
        elif y21 < y12:
            return y12 - y21
    
    elif y11 <= y12 <= y21 or y11 <= y22 <= y21:
        
        # only horizontal separation
        if x11 > x22:
            return x11 - x22
            
        elif x21 < x12:
            return x12 - x21
            
    elif x11 > x22:
        
        # house2 is left above house1
        if y11 > y22:
            return ((y11 - y22) ** 2 + (x11 - x22) ** 2) ** 0.5
        
        # house2 is left below house1
        elif y21 < y12:
            return ((y12 - y21) ** 2 + (x11 - x22) ** 2) ** 0.5
            
    elif x21 < x12:
        
        # house2 is right above house1
        if y11 > y22:
            return ((y11 - y22) ** 2 + (x12 - x21) ** 2) ** 0.5
        
        # house2 is right below house1
        elif y21 < y12:
            return ((y12 - y21) ** 2 + (x12 - x21) ** 2) ** 0.5
    
    # error
    else:
        return -1