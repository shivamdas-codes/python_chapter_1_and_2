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

