# """# (1).Given an integer, n , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird"""

# n = 24
# if(n is "odd" and "odd numbers are weird"):
#     print("weird")
# elif(n is "even" and n in range(2,5)):
#     print("not weird")
# elif(n is "even" and n in range(6,20)):
#     print("weird")
# else:
#     (n > 20 and n is "even")
#     print("not weird")

    

# """The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers."""

# a = int(input())
# b = int(input())
# sum = (a + b)
# diff = (a - b)
# prod = (a * b)
# print(sum,diff,prod)



"""The provided code stub reads two integers, a and b, from STDIN.Add logic to print two lines. 
The first line should contain the result of integer division, a // b. 
The second line should contain the result of float division, a / b.
No rounding or formatting is necessary."""

a = int(input())
b = int(input())
num1 = (a // b)
num2 = (a / b)
print(num1)
print(num2)