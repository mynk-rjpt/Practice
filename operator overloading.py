# Operator Overloading roughly means to make a python predefined Operator usable accoding to our needs in a class,
# to make a program more eligant. Although the predefined function of the operator will still be usable along with 
# a new function that it can perform

class Point() :
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def printPoint(self) :
        print(f"({self.x},{self.y})")    

    def __sub__(self, other) :
        return(f"({self.x - other.x},{self.y - other.y})")

point1 = Point(3,4)
point2 = Point(5,6)

point1.printPoint() 
point2.printPoint()
point3 = point2 - point1
print(point3)

