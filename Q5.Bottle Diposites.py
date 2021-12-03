


#PROCESS 1:
n=int(input("enter the no of bottels :"))
l=[]
for i in range(0,n):
    l.append(float(input("enter the volume :")))

r=0
for j in l:
    if(j<= 1):
        r=r+0.1
    else:
        r=r+.25
print ("Total refund will be {:.2f}".format(r))

#PROCESS 2:


