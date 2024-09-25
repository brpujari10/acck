#creating sample class rectangle with a constructor which includes 2 properties length and width.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    #implementing customization using __iter__ magic method to yield the length and width automatically
    #when we iter into rectangle class object. 
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


rect = Rectangle(5, 3)
for item in rect:
    print(item)

