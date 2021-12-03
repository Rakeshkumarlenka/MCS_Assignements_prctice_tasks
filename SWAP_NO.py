class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def swap(self):
        temp = self.a
        self.a = self.b
        self.b = temp

    def display(self):
        print("After swap a is:", self.a)
        print("After swap b is:", self.b)


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Test(a, b)
obj.swap()
obj.display()