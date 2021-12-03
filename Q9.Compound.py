
#PROCESS 1:
# amount = float(input("Enter the amount"))
# yr1=amount+(amount*0.04)
# yr2=yr1+(yr1*0.04)
# yr3=yr2+(yr2*0.04)
# print("amount of 1st year = {}".format(yr1))
# print("amount of 2st year = {}".format(yr2))
# print("amount of 3st year = {}".format(yr3))

# amount = float(input("Enter the amount"))
# # yr1=amount+(amount*0.04)
# # yr2=yr1+(yr1*0.04)
# # yr3=yr2+(yr2*0.04)
# t=raw_input("enter the time period")
# intrest = amount +(amount*0.04*t)
# print("amount of year = {}".format(intrest))
# # print("amount of 2st year = {}".format(yr2))
# # print("amount of 3st year = {}".format(yr3))



#PROCESS 2:
amount = float(input("Enter the savings account amount"))
amount1yr= amount*((1+(0.04))**1)
amount2yr= amount*((1+(0.04))**2)
amount3yr= amount*((1+(0.04))**3)
print("amount of 1st year = {}".format(amount1yr))
print("amount of 2st year = {}".format(amount2yr))
print("amount of 3st year = {}".format(amount3yr))


