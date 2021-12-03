fullmarks=int(input("Enter the full marks :"))
marks=[]
for i in range(1,7):
    y=int(input("Enter marks of students:"))
    marks.append(y)

sum=0
for j in marks:
    sum=sum+j
print(sum)

avgtotal=sum /(fullmarks*6)*100
print(avgtotal)

marks.sort(reverse=True)
print(marks)

totalof3=marks[0]+marks[1]+marks[2]
print(totalof3)

avgtotalof3=totalof3/(fullmarks*3)*100
print(avgtotalof3)

if avgtotalof3 >95:
    print("gold medal")
if avgtotal>90:
    print("distnction")
elif 75 < avgtotal < 90:
    print("Average")
else:
    print("fail")
