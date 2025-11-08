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
