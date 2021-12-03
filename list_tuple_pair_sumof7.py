
num = []
flag2 = 1

while(flag2):
    try:
        if (flag2 != -1):
            n = input("Enter number : ")
            num.append(int(n))
        an_no = input("Do you want to enter another no (y/n) : ")
        if (an_no == "y"):
            flag2 = 1     #it will b again cont. loop and ent no n an_no opt
        elif (an_no == "n"):
            flag2 = 0     #it will b out of loop
        else:
            print("WRONT INPUT  ")
            flag2 = -1    #it will b again cont loop and it will print out of if block

    except:
        print("Not valid input. Enter integers only : ")

print("-------------------------------------------------")
print("Total inputs were by user \n ",num)
print("-------------------------------------------------")
print("After remove duplicate new list \n",set(num))
print("-------------------------------------------------")

output = []
i = 0
while(i<(len(set(num))-1)):
    j = i+1
    pair_found = 0
    while(j < len(num)):
        num1 = num[i]
        num2 = num[j]
        if((num1+num2) == 7):
            pair_found = 1
            z = (num1,num2)
            output.append(z)
            num.remove(num1)
            num.remove(num2)
            break
        j += 1
    if(pair_found == 1):
        continue
    else:
        i += 1

print("-------------------------------------------------")
print("sum of 7 pair of no _tuple _list is :\n",output)
print("-------------------------------------------------")

print("After remove duplicate pairs list is :\n",(set(output)))

print("-------------------------------------------------")