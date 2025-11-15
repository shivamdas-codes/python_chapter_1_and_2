# this code indicates about the conditional statements in python, which is mainly used in decision making
# example code 1
light = input("light colour =")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("get ready")
elif(light == "green"):
    print("go")
else:
    print("if light is broken")


# example code 2
marks = input("marks :")
if(marks >= "90"):
    print("grade A")
elif(marks >= "80" and marks < "90"):
    print("grade B")
elif(marks >= "70" and marks < "80"):
    print("grade C")
else:
    print("fail")
# in the above code the input statement always return the string not the integer value
# in the code the "and" operator is used to combine two conditions together


# example code 3
a = input("a :")
g = input("f/m :")
if((a == 2 or a == 1) and g == "m"):
    print("fee is 200")
elif(a == 3 or a == 5 or g == "f"):
    print("fee is 300")
elif(a == 4 and g == "m"):
    print("fee is 400")
else:
    print("no fee")



# this codes comes under ternary operator also known as the single line comment in python 
# we can write in two ways 
food = input("food :")
order = "yes" if food == "cake" else "no"
print(order)

# first by assigning the variable value in it 

food = input("food :")
print("sweet") if(food == "cake" or food == "icecream") else print("not sweet")
# second by directly using print statement in it




# this code also part of the ternary operator but in different way, also known as the "clever if" statement
a = int(input("age :"))
vote = ("yes","no") [a >= 18]
print(vote)




# we can write a clever if statement in 2 ways...
sal = float(input("salary :"))
tax = sal *(0.1,0.2) [sal > 50000]
print(tax)

sal = float(input("salary :"))
tax = sal * (0.1 if sal <= 50000 else 0.2)
print(tax)




# Example program :
# HACKERRANK PRACTICE PROBLEM
"""# (1).Given an integer, n , perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird"""

n = 24
if(n is "odd" and "odd numbers are weird"):
    print("weird")
elif(n is "even" and n in range(2,5)):
    print("not weird")
elif(n is "even" and n in range(6,20)):
    print("weird")
else:
    (n > 20 and n is "even")
    print("not weird")



# part- 2
age = int(input("enter your age: "))
if (age < 18):
    print("you are a minor")
elif (age >= 18 and age < 65):
    print("you are an adult")
else:
    print("you are a senior citizen")



num = 100
if(num >= 2):
    print("true")
if(num < 10):
    print("true")   
if(num == 5):
    print("true")
elif(num != 5):
    print("false")
else:
    print("none")



voter_age = int(input("Enter your age: "))
if voter_age >= 18:
    print("You are eligible to vote.")
# if voter_age < 18:
#     print("You are not eligible to vote.")    
# elif voter_age == 18:
#     print("You have just become eligible to vote.")
else:
    print("Invalid age entered.")    

   

# NESTED IF STATEMENT
# example 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
    citizenship = input("Are you a citizen? (yes/no): ")
    if citizenship.lower() == "yes":
        print("You can register to vote.")
    else:
        print("You must be a citizen to register to vote.")


# example 2
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print("Grade: A")
    if marks >= 95 and marks < 100:
        print("Excellent performance!")
        if marks == 100:
            print("Perfect score!")
elif marks >= 80 and marks < 90:
    print("Grade: B")
else:
    print("Good job!")


# # example 3
num = 75
if num % 5 == 0:
    if num % 2 == 0:
        print("java")
    else:
        print("python")
else:
    print("c++")

