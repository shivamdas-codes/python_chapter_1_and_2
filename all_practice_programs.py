#(1).write a program to input 2 numbers and print their sum, difference, product, quotient and remainder
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

sum_result = number1 + number2
difference_result = number1 - number2
product_result = number1 * number2
quotient_result = number1 / number2
remainder_result = number1 % number2

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)



#(2).write a program to input side of a square and print its area and perimeter
side1 = float(input("Enter the square side1: "))
side2 = int(input("Enter the square side2: "))
side3,side4 = int(input("Enter perimeter of the square side3: ")), (input("Enter perimeter of the square side4: "))

area = side1 * side1
print("square side:", side2 ** 2)
print("Area of square:", area)
print("Perimeter of square:", 4 * side3,4 * side4)



#(3).write a program to input 2 floating point numbers and print their average
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

the_average = (num1 + num2) / 2
print("Average:", the_average)
print("Average:", (num3 + num4) / 2)



#(4).write a program to input 2 int numbers, a and b print true if a is greater than or equal to b otherwise print false
var_a  = int(input("Enter first integer (a): "))
var_b  = int(input("Enter second integer (b): "))
if var_a >= var_b:
    print("True")
else:
    print("False")



# (5).write a program to input users first name and print its length
user_1 = input("first name :")
firstname = len(user_1)
print(firstname)
print(len(user_1))   # prints the length of the string



# (6).write a program to find the occerrences of S in a string
str1 = input("enter string :")
count = str1.count("s")
print("Occurrences of 's':", count)   # prints the number of occurrences of 's' in the string

str2 = "this is shivam das"
print(str2.count("s"))   # prints the number of occurrences of 's' in the string


# (11).write a program to ask the user to enter the names of their 3 fav movies and store them in a list
movies_list = []
num1 = input("enter the first movie: ")
num2 = input("enter the second movie: ")
num3 = input("enter the third movie: ")
movies_list.append(num1)
movies_list.append(num2)
movies_list.append(num3)
print(movies_list)
# or
movies_list1 = []
num = input("enter 1st movie: ")
movies_list1.append(num)
num = input("enter 2nd movie: ")
movies_list1.append(num)
num = input("enter 3rd movie: ")
movies_list1.append(num)
print(movies_list1)
# or
movies_list2 = []
movies_list2.append(input("enter 1st movie: "))
movies_list2.append(input("enter 2nd movie: "))
movies_list2.append(input("enter 3rd movie: "))
print(movies_list2)
