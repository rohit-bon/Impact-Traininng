class area():
    def __init__(self,height,breadth):
        self.height = height
        self.breadth = breadth
    
    def display_area(self):
        area = self.height*self.breadth/2
        print("Area of triangle:",area)
        
triangle = area(12,10)
triangle.display_area()


# o/p:
# Area of triangle: 60.0