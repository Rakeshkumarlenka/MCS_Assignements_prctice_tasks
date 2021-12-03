
#PROCESS 1:
# n = int (input ("Enter the integer: "))
# sm = n * (n + 1) / 2
# print ("The sum of the first", n, " integers is", sm)


#PROCESS 2:

n = int(input("Enter the integer : "))
sum = 0
for i in range(1,(n+1)):
    sum += i
print("Sum for 1 to ",n," = ",sum)