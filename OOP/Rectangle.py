class Rectangle:
    def __init__(self, length=None, width=None):
        self.__length = length
        self.__width = width

    def area(self):
        print(self.__length * self.__width)

    def parameters(self):
        print(2 * (self.__length + self.__width))


rectangle = Rectangle(4, 5)
rectangle.area()
rectangle.parameters()
