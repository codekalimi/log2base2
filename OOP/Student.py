class Student:
    def __init__(self):
        self.__rollNumber = None
        self.__name = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


student = Student()
print(student.getName())
student.setName("Aamir Kalimi")
print(student.getName())
