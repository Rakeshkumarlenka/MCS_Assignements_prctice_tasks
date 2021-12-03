class Complex:
    def __init__(self,a,b):
        self.real = a
        self.imag = b

    def shw_no(self):
        print("number =",self.real ,"+ i " , self.imag )

def sum(num1,num2):
    num3 = Complex(0,0)
    num3.real=num1.real + num2.real
    num3.imag =num1.imag + num2.imag
    return num3

num1 = Complex(2,3)
num1.shw_no() #object.method
num2 = Complex(4,5)
num2.shw_no()
result = sum(num1, num2)
result.shw_no()








