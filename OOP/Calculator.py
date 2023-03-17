class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print(self.num1 - self.num2)

    def multiplication(self):
        print(self.num1 * self.num2)

    def division(self):
        print(self.num1 / self.num2)


calculator = Calculator(20, 10)
calculator.add()
calculator.subtract()
calculator.multiplication()
calculator.division()
