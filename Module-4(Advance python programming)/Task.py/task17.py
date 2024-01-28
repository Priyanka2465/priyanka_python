# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

# Ans. Inheritance allows us to define a class that inherits all the methods and properties from another class...
# Constructors in Python is a special class method for creating and initializing an object instance at that class.

class Father():
    def farm(self):
        print("Father's Farm")

class Son(Father):
    def house(Self):
        print("Son's House")

obj=Son()
obj.farm()
obj.house()
 
