# #(1).write a program to input 2 numbers and print their sum, difference, product, quotient and remainder
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))

# sum_result = number1 + number2
# difference_result = number1 - number2
# product_result = number1 * number2
# quotient_result = number1 / number2
# remainder_result = number1 % number2

# print("Sum:", sum_result)
# print("Difference:", difference_result)
# print("Product:", product_result)
# print("Quotient:", quotient_result)
# print("Remainder:", remainder_result)



# #(2).write a program to input side of a square and print its area and perimeter
# side1 = float(input("Enter the square side1: "))
# side2 = int(input("Enter the square side2: "))
# side3,side4 = int(input("Enter perimeter of the square side3: ")), (input("Enter perimeter of the square side4: "))

# area = side1 * side1
# print("square side:", side2 ** 2)
# print("Area of square:", area)
# print("Perimeter of square:", 4 * side3,4 * side4)



# #(3).write a program to input 2 floating point numbers and print their average
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))

# the_average = (num1 + num2) / 2
# print("Average:", the_average)
# print("Average:", (num3 + num4) / 2)



# #(4).write a program to input 2 int numbers, a and b print true if a is greater than or equal to b otherwise print false
# var_a  = int(input("Enter first integer (a): "))
# var_b  = int(input("Enter second integer (b): "))
# if var_a >= var_b:
#     print("True")
# else:
#     print("False")



# # (5).write a program to input users first name and print its length
# user_1 = input("first name :")
# firstname = len(user_1)
# print(firstname)
# print(len(user_1))   # prints the length of the string



# # (6).write a program to find the occerrences of S in a string
# str1 = input("enter string :")
# count = str1.count("s")
# print("Occurrences of 's':", count)   # prints the number of occurrences of 's' in the string

# str2 = "this is shivam das"
# print(str2.count("s"))   # prints the number of occurrences of 's' in the string



# # (7).write a program to input the grades of a students based on marks
# student_marks = int(input("Enter your marks: "))
# if student_marks >= 90:
#     print("Grade: A")
# elif student_marks >= 80 and student_marks < 90:
#     print("Grade: B")
# elif student_marks >= 70 and student_marks < 80:
#     print("Grade: C") 
# elif student_marks >= 60 and student_marks < 70:
#     print("Grade: D")  
# else:
#     grade = "Fail"
#     print("Grade:", grade)
    


# # (8).write a program to check if a number is entered by the user is even or odd
# num = int (input("Enter a number: "))
# rem = num % 2
# if rem == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")



# # (9).write a program to find the greatest among 3 numbers entered by the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# num4 = int(input("Enter fourth number: "))

# if num1 >= num2 and num1 >= num3:
#     greatest = num1
#     print("The greatest number is a:", num1)
# elif num2 >= num1 and num2 >= num3:
#     greatest = num2
#     print("The greatest number is b:", num2)  
# elif num3 >= num1 and num3 >= num2:
#     greatest = num3
#     print("The greatest number is c:", num3)
# elif num4 >= num1 and num4 >= num2 and num4 >= num3:
#     greatest = num4
#     print("The greatest number is d:", num4)
# else:
#     print("All numbers are equal.")



# # (10).write a program to check if a number is multiple of 7 or not
# num = int(input("Enter a number: "))
# rem = num % 7
# if rem == 0:
#     print("The number is a multiple of 7.")
# else:
#     print("The number is not a multiple of 7.")
# # or
# a = int(input("Enter first number: "))
# if a % 7 == 0:
#     print("Multiple of 7")
# else:
#     print("Not a multiple of 7")
    


# # (11).write a program to ask the user to enter the names of their 3 fav movies and store them in a list
# movies_list = []
# num1 = input("enter the first movie: ")
# num2 = input("enter the second movie: ")
# num3 = input("enter the third movie: ")
# movies_list.append(num1)
# movies_list.append(num2)
# movies_list.append(num3)
# print(movies_list)
# # or
# movies_list1 = []
# num = input("enter 1st movie: ")
# movies_list1.append(num)
# num = input("enter 2nd movie: ")
# movies_list1.append(num)
# num = input("enter 3rd movie: ")
# movies_list1.append(num)
# print(movies_list1)
# # or
# movies_list2 = []
# movies_list2.append(input("enter 1st movie: "))
# movies_list2.append(input("enter 2nd movie: "))
# movies_list2.append(input("enter 3rd movie: "))
# print(movies_list2)



# # (12).write a program to check if a list contains a "palindrome" of elements (hint: use copy() method)
# list1 = [2,3,3,2]  # this is a palindrome list
# list2 = [5,6,4,1]  # this is not a palindrome list
# list3 = ["m", "a", "a", "m"]

# copylist1 = list1.copy()
# copylist1.reverse()
# # if you want to check wheather the given condition is palindrome or not first you have to copy() and then reverse() the given condition.
# copylist2 = list2.copy()
# copylist2.reverse()
# # if you want to check wheather the given condition is palindrome or not first you have to copy() and then reverse() the given condition.
# copylist3 = list3.copy()
# copylist3.reverse()
# # if you want to check wheather the given condition is palindrome or not first you have to copy() and then reverse() the given condition.
# if (copylist1 == list1):
#     print("its a palindrome")
# else:
#      print("not a palindrome")

# if (copylist2 == list2):
#         print("its a palindrome")
# else:
#     print("not a palindrome")

# if(copylist3 == list3):
#      print("its a palindrome")
# else:
#      print("not a palindrome")



# # (13).write a program to count the number of students with the "A" grade in the following tuple
# students_grades = ("A", "B", "C", "A", "A")
# print(type(students_grades))   # type of the variable
# print(len(students_grades))   #lenght of the variable
# print(students_grades.count("A"))



# # (14).store the above value in a list and sort them from "A" to "D"
# list = ["A", "C", "B", "D", "C", "A", "B", "D"]
# list.sort()
# print(list)



# # (15).store the following word meaning in a pyhton dictionary
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ("a piece of furniture", "list of facts and figures"),

#     "time_table" : {
#         "breakfast" : "8:00 to 9:00",
#         "lunch" : ("12:00", "to", "1:00"),
#         "dinner" : [7,8] 
#     }  #the syntax in the dictionary are very strict
# }
# print(dictionary)



# # (16).you are given a list of subjects for students. assume one calssroom is required for 1 subject. how many classroom are needed by all students?
# set1 = {"python", "java", "cpp", "python", "js"}
# set2 = {"java", "python", "java", "cpp", "c"}
# print(set1.union(set2))
# # even the above code also written correctly but instead of finding lenght we assumed the subjects as 2 sets. 
# print(len(set1.union(set2))) # by using the lenght function we can say that how many classrooms needed for each subjects.



# # (17).write a program to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and add one by one.use subject name as key and marks as value.
# student_marks = {}  # an empty dictionary
# subject1 = int(input("enter maths :"))
# student_marks.update({"maths" : subject1})

# subject2 = int(input("enter science :"))
# student_marks.update({"science" : subject2})

# subject3 = int(input("enter english :"))
# student_marks.update({"english" : subject3})
# print(student_marks)
# #DOUBT: IF I GIVE SAME VARIABLE FOR ALL THE VALUES WILL IT OVER RIDE?
# #NOTE: IF WE ENTER/GIVE THE SAME VARIABLE FOR THE ALL THREE INPUTS IT WILL TAKE SEPERATELY AND DONT OVERRIDE WITH EACH OTHER, THE OVERRIDE IS POSSIBLE WHEN THE KEY IS SAME NOT THE VARIABLE



# # (18).figure out a way to store 9 and 9.0 as seperate values in a set.(hint: take help of builtin data types)
# value = {9, 9.0}
# print(value)
# """ we know that the first value id integer and the second value is float
#  in python it will take both the values as same values
#  in set we cant print both the values as different values it will take both the values as the same number if that number is assigned by "0" after decimal"""

# values = {9, "9.0"}
# print(values)
# # in this case we can able to print both the values as seperate values because one of the values is consider as string and the other as integer

# values1 = {("float", 9.0),("int", 9)}
# print(values1)
# # in this case we can able to print our both the values because they were assigned by their original data types
# # in this way also we can print two different values



# # WHILE LOOP:
# # (19). print number from 1 to 100
# i = 1
# while i <= 100:
#     print(i)
#     i +=1


# # (20). print numbers from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1


# # (21). print the multiplication table of a number n
# n = int(input("enter the number:")) # user input [ the input which is given is the fixed input and there is no change in that input]
# i = 1       #starting point from where the loop will start and it can be changed
# while i <= 10:  #ending point where the loop will end and it can be changed too
#     print(n*i)  # 'n' is given input and 'i' is the variable which is changing every time
#     i += 1
# # so, basically we shouldn't assign the 'n' value in the loop because it is a fixed value and 'i' is the variable which is changing every time the loop takes place.


# # (22). print the elements of a list using while loop
# list = [1,4,9,16,25,36,49,64,81,100]
# index = 0   # index always starts from 0
# while index < len (list):  # len(list) = 10
#     print(list[index])   # prints the element at the current index
#     index += 1           # move to the next index


# (23).search for a number "x" in this tuple using loop
tuple = (1,4,9,16,25,36,49,64,81,100,1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the number to search:"))
i = 0   #initialization
while i < len(tuple):
    if tuple[i] == x:
        print("found the index:",i)
    else:
        print("keep finding")   #it keeps finding till the last index though the value is found or not found
# its not nesassary to use the else statement in this case 
    i += 1
