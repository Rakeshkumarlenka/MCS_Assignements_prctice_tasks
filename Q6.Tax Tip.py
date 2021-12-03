#PROCESS:1

# cost = float(input("Enter the cost of meal : "))
# tax = cost*12/100
# tip = cost*18/100
# grand_total = cost + tax + tip
# print("Grand Total = {:.2f}\nTax = {:.2f}\nTip = {:.2f}".format(grand_total,tax,tip))


#PROCESS: 2
TAX_RATE = 0.05
TIP_RATE = 0.18
cost = float (input ("Enter the cost of the meal: "))
tax = cost * TAX_RATE
tip = cost * TIP_RATE
total = cost + tax + tip
print ("tax is", tax)
print ("tip is", tip)
print ("total cost is", total)