class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        total = self.phy + self.chem + self.bio
        return total


calculateStudentPerformance = Student("Aamir Kalimi", 90, 30, 50)
print(calculateStudentPerformance.bio)
print(calculateStudentPerformance.totalObtained())
