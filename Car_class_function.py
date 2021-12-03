class Car:
    def __init__(self,x,a,b,c,d):
        self.name = x
        self.color = a
        self.wheel = b
        self.door = c
        self.cngorpetrol= d

    def show_car(self):
        print("name=",self.name)
        print("color=",self.color)
        print("wheel =",self.wheel)
        print("door =",self.door)
        print("cng or petrol=",self.cngorpetrol)

    def speed(self,c_speed):
        print(c_speed)

car1= Car("hundai","white",4,4,"petrol")
car1.show_car()

speed1=int(input("enter the speed :"))
car1.speed(speed1)
