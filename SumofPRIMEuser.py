list=[]
for i in range(1,11):
    a=int(input("Enter the values :"))
    list.append(a)
print (list)
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

print(sumofprime)

    
    


