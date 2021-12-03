list=[]
for i in range(1,11):
    a=int(input("Enter the values :"))
    list.append(a)
print (list)
even=0
odd = 0
for j in list:
    if (j % 2==0):
        even=even + j
    else:
        odd=odd + j

prime=[]
sumofprime=0
for j in list:
    count=0
    i=1
    while (i<=j):
        if(j % i) ==0:
            count=count+1
        i=i+1
    if(count==2):
        prime.append(j)
print(prime)

for i in prime:
    sumofprime = sumofprime + i

print ("Sum of total sum of even no inputs :",even)2
print ("Sum of total sum of odd no inputs :",odd)
print ("Sum of total sum of prime no inputs :",sumofprime)

        
    

