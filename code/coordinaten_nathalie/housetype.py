from houses import house

class eengezins(house):
    
    def __init__(self, x1, y1):
        
        self.width = 8
        self.length = 8
        self.basicValue = 285000
        self.freeSpace = 2
        self.extraValue = 0.03 * self.basicValue
        house.__init__(self, x1, y1)

class bungalow(house):
    
    def __init__(self, x1, y1):
        
        self.width = 7.5
        self.length = 10
        self.basicValue = 399000
        self.freeSpace = 3
        self.extraValue = 0.04 * self.basicValue
        house.__init__(self, x1, y1)
        
class maison(house):
    
    def __init__(self, x1, y1):
        
        self.width = 10.5
        self.length = 11
        self.basicValue = 610000
        self.freeSpace = 6
        self.extraValue = 0.06 * self.basicValue
        house.__init__(self, x1, y1)