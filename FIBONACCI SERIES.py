# def Fibonacci(n):
#     # Check if input is 0 then it will
#     # print incorrect input
#     if n < 0:
#         print("Incorrect input")
#
#     # Check if n is 0
#     # then it will return 0
#     elif n == 0:
#         return 0
#
#     # Check if n is 1,2
#     # it will return 1
#     elif n == 1 or n == 2:
#         return 1
#
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
#
# print(Fibonacci(9))

n_terms = int(input("How many terms the user wants to print? "))

# First two terms
n_1 = 0
n_2 = 1
count = 0

# Now, we will check if the number of terms is valid or not
if n_terms <= 0:
    print("Please enter a positive integer, the given number is not valid")
# if there is only one term, it will return n_1
elif n_terms == 1:
    print("The Fibonacci sequence of the numbers up to", n_terms, ": ")
    print(n_1)
# Then we will generate Fibonacci sequence of number
else:
    print("The fibonacci sequence of the numbers is:")
    while count < n_terms:
        print(n_1)
        nth = n_1 + n_2
        # At last, we will update values
        n_1 = n_2
        n_2 = nth
        count += 1