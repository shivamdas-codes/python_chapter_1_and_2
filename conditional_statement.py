# # this code indicates about the conditional statements in python, which is mainly used in decision making
# # example code 1
# light = input("light colour =")
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("get ready")
# elif(light == "green"):
#     print("go")
# else:
#     print("if light is broken")


# # example code 2
# marks = input("marks :")
# if(marks >= "90"):
#     print("grade A")
# elif(marks >= "80" and marks < "90"):
#     print("grade B")
# elif(marks >= "70" and marks < "80"):
#     print("grade C")
# else:
#     print("fail")
# # in the above code the input statement always return the string not the integer value
# # in the code the "and" operator is used to combine two conditions together


# # example code 3
# a = input("a :")
# g = input("f/m :")
# if((a == 2 or a == 1) and g == "m"):
#     print("fee is 200")
# elif(a == 3 or a == 5 or g == "f"):
#     print("fee is 300")
# elif(a == 4 and g == "m"):
#     print("fee is 400")
# else:
#     print("no fee")



# # this codes comes under ternary operator also known as the single line comment in python 
# # we can write in two ways 
# food = input("food :")
# order = "yes" if food == "cake" else "no"
# print(order)

# # first by assigning the variable value in it 



# # SINGLE LINE:
# food = input("food :")
# print("sweet") if(food == "cake" or food == "icecream") else print("not sweet")
# # second by directly using print statement in it


# # this code also part of the ternary operator but in different way, also known as the "clever if" statement
# a = int(input("age :"))
# vote = ("yes","no") [a >= 18]
# print(vote)



# # CLEVER IF:
# # we can write a clever if statement in 2 ways...
# sal = float(input("salary :"))
# tax = sal *(0.1,0.2) [sal > 50000]
# print(tax)

# sal = float(input("salary :"))
# tax = sal * (0.1 if sal <= 50000 else 0.2)
# print(tax)



# # part- 2
# age = int(input("enter your age: "))
# if (age < 18):
#     print("you are a minor")
# elif (age >= 18 and age < 65):
#     print("you are an adult")
# else:
#     print("you are a senior citizen")



# num = 100
# if(num >= 2):
#     print("true")
# if(num < 10):
#     print("true")   
# if(num == 5):
#     print("true")
# elif(num != 5):
#     print("false")
# else:
#     print("none")



# voter_age = int(input("Enter your age: "))
# if voter_age >= 18:
#     print("You are eligible to vote.")
# # if voter_age < 18:
# #     print("You are not eligible to vote.")    
# # elif voter_age == 18:
# #     print("You have just become eligible to vote.")
# else:
#     print("Invalid age entered.")    

   

# # NESTED IF STATEMENT
# # example 1
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
#     citizenship = input("Are you a citizen? (yes/no): ")
#     if citizenship.lower() == "yes":
#         print("You can register to vote.")
#     else:
#         print("You must be a citizen to register to vote.")


# # example 2
# marks = int(input("Enter your marks: "))
# if marks >= 90 and marks <= 100:
#     print("Grade: A")
#     if marks >= 95 and marks < 100:
#         print("Excellent performance!")
#         if marks == 100:
#             print("Perfect score!")
# elif marks >= 80 and marks < 90:
#     print("Grade: B")
# else:
#     print("Good job!")


# # # example 3
# num = 75
# if num % 5 == 0:
#     if num % 2 == 0:
#         print("java")
#     else:
#         print("python")
# else:
#     print("c++")


# # SHORT CIRCUIT EVALUATION IN LOGICAL OPERATORS
# years = 5
# if True or False:
#     years = years + 2
# print(years)

# # -----------------------------------------------------------------------------------------------------------------------

# # to find wheather the numbers are positive,negative or zero
# var = int(input("enter number:"))
# if var > 0:
#     print("positive")
# elif var < 0:
#     print("negative")
# else:
#     print("zero") 
# # just normal code to find the single element is (+,- or 0)



# num = int(input("enter a number:"))
# if num % 2 == 0:
#     print("even")
# elif num % 2 != 0:
#     print("odd")
# else:
#     print("the value is not a even not a odd")
# # even or odd


# num1 = input("enter a number:")
# if num1.isdigit():  #this line only works if there is only strings that too any number inside the string.
#     num1 = int(num1)
#     if num1 % 2 == 0:
#         print("its even")
#     else:
#         print("its odd")
# else:
#     print("not a valid number")
# # even or odd with else statement



# voting_age = int(input("enter your age:"))
# if voting_age > 18:
#     print("you are completely eligible to vote")
# elif voting_age == 18:
#     print("recently eligible \nyes you can vote")
# else:
#     print("dont waste time here \nyou are not eligible")
# # eligible for voting or not



# var = int(input("enter a number:"))
# if var % 5 == 0:
#     print("divisible by 5")
# else:
#     print("not divisible by 5 ")
# # divisible by 5 or not



# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# if a > b:
#     print("a is largest number")
# else:
#     print("b is largest number")
# # largest of two numbers

# # ----------------------------------------------------------------------------------------------------------------------


# num1 = int(input("number1:"))
# num2 = int(input("number2:"))
# num3 = int(input("number3:"))
# if num1 > num2 and num1 > num3: #here num1 is greater than both num2 and num3
#     print("num1 is largest")
# elif num2 > num3 and num2 > num1:   #here num2 is greater than both num3 and num1
#     print("num2 is largest")
# else:
#     print("num3 is largest")
# # When comparing multiple numbers, each comparison must be explicit.    {for example: a>b and a>c}



# char = input("enter any letter:")
# vowels = ("a","i","o","u","e")
# if char in vowels:
#     print("this char is vowel")
# else:
#     print("not a vowel \nit is consonants")
# # checking wheather the letter is vowel or not.



# num = int(input("enter a number:"))
# if num%3==0 and num%7==0:
#     print("yes it is divisible by both")
# else:
#     print("not divisible")
# # divisible by 3 and 7 or not.


# number = int(input("enter a number:"))
# if number == 2:
#     print("prime number")
# elif number == 3:
#     print("prime number")
# elif number > 1 and number % 2 != 0 and number % 3 != 0:
#     print("ita a prime number")
# else:
#     print("its not a prime number")
# this conditions are not enough to find wheather to find a number is prime number or not.