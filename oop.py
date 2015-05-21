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
    
#executed at runtime 
#give me an object from the Shape class
#set its 'name' property to 'square'
#square = Shape('square')
#print square.name 

square = Square('square',4)
print square.name
print square.side
