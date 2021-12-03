
# PROCESS 1:
#
# length = float (input ("Enter the length of the room in feet: "))
# width = float (input ("Enter the width of the room in feet: "))
# area = length * width
# print ("The area of the room is", area, "square feet")

#PROCESS 2:
l = float(input('Enter the length of a room: '))
b = float(input('Enter the breadth of a room: '))
Area = l * b
meter = Area *0.3048
print("Area of the room in squarefeet: %.2f" %Area)
print("Area of the room in meter: %.2f" %meter)