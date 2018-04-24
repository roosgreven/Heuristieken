class house:
    
    def __init__(self, x1, y1):
        
        self.x1 = x1
        self.x2 = x1 + self.width
        self.y1 = y1
        self.y2 = y1 + self.length
        self.totalValue = self.basicValue
        
    def value(self, distance):
        
        extraFreeSpace = distance - self.freeSpace
        
        self.totalValue = self.basicValue + self.extraValue * extraFreeSpace
        
    def coordinates(self, x1, y1):
        
        self.x1 = x1
        self.x2 = x1 + self.width
        self.y1 = y1
        self.y2 = y1 + self.length
        
    def test(self):
        print(self.x1)
        print(self.x2)
        print(self.y1)
        print(self.y2)
        