# Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle...
class Rectangle():
    def __init__(self,length,width):
        self.l=length
        self.w=width

    def disp(self):
        print("Area of Rectangle=",self.l*self.w)

obj=Rectangle(12,6)
obj.disp()