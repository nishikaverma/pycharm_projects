import math
class circle:
    def __init__(self,radious):
        self.radious=radious
    def area(self,radious):
        print("the area  of circle with radious ",radious,"cm's is",math.pi*math.pow(self.radious,2))