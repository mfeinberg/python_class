from math import pi

class Shape(object): #object means it inherits from the type object, which is a built in class
    
    name = 'shape' #attached to the shape class itself, applies to every single object created using this class
    
    #def __init__(self,name): #when I create a shape I must give it a name
    #    self.name = name
        
    def speak(self):
        print 'I am a ',self.name

class Square(Shape):
    
    def __init__(self,name,side):
        self.name = name #inheritance: will look up local, if no local will go up to find property in parent
        self.side = side
        
    #def speak(self):
   #     super(Square,self).speak()
        
    def get_area(self):
        side = self.side
        return side*side

class Circle(Shape):
    
    def __init_(self,name,radius):
        self.name = name
        self.radius = radius
        
    def get_area(self):
        return pi * (self.radius**2)
#executed at runtime 
#give me an object from the Shape class
#set its 'name' property to 'square'
#square = Shape('square')
#print square.name 

square = Square('square',4)
print square.name
print square.side
print square.get_area()
super(Square,square).speak() #Square has no speak method, but super() tells it to go the
print isinstance(square,Circle)
print hasattr(square,'speaks')
