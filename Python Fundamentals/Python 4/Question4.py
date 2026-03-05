from abc import ABC , abstractmethod
class Shape (ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        print (f"The area of given circle is {3.14*self.radius*self.radius}")

class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width
    def area(self):
        print (f"The area of given rectangle is {self.length*self.width}")

class Triangle(Shape):
    def __init__(self , base , height):
        self.base = base
        self.height = height 
    def area(self):
        print (f"The area of given traingle is {0.5 * self.base *self.height}")

   # Creating objects
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(3, 8)

# Calling methods
c.area()
r.area()
t.area()