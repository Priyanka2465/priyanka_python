# Write a Python class named Circle constructed by a radius and two
# methods which will compute the area and the perimeter of a circle...
class Circle():
    def __init__(self,r):
        self.r=r

    def area(self):
        print(self.r**2*3.14)

    def perimeter(self):
        print(2*self.r*3.14)

obj=Circle(8)
obj.area()
obj.perimeter()
