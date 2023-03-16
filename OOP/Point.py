# Implement a class Point that has three properties and a method. All these attributes (properties and methods) should be public. This problem can be broken down into two tasks:
class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def sqr_sum(self):
        calculate_sqr_sum = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        return calculate_sqr_sum


point = Point(4, 2, 5)
print(point.sqr_sum())
print(point.x)
