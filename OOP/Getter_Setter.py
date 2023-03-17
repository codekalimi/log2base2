class User:
    def __init__(self, username=None):
        self.__username = username

    def setUserName(self, name):
        self.__username = name

    def getUserName(self):
        return self.__username


user = User("Aamir Kalimi")
print(user.getUserName())
user.setUserName("Imran Kalimi")
print(user.getUserName())
