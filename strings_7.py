# the strings can be written in three ways
str1 = 'hello world'          # using single quotes
str2 = "hello world"          # using double quotes
str3 = '''hello world'''        # using triple quotes



# escape sequence in strings
str1 = "hey this is shivam das\ncurrently im pursuing my mca"
# the above line was assigned by '\n' which is used to break the line in the output as two sentences
str2 = "hey this is shivam das\tcurrently im pursuing my mca"
# the above line was assigned by '\t' which is used to give a tab space in the output
print(str1 )
print(str2 )


#1.concatenation of strings
str1 = "hello "
str2 = "world"
final_string = str1 + str2
print(final_string)


#2.lenghth of the string
str1 = "hello world"
print(len(str1))
str2 = "shivam das"
print(len(str2))
print(str1 + " " + str2)
print(len(str1 + " " + str2))


#3.indexing in strings
str1 = "hello world"
print(str1[0])   # first character
print(str1[4])   # fifth character
char = str1[6]
print(char)      # seventh character
# this is called positive indexing in strings 


"""# str = "hello world"
# str[5] =  'W'   # this will give error because strings are immutable in python
# print(str)"""



#4.slicing in strings
str = "hello world"
print(str[1:5])    # prints characters from index 0 to 4
print(str[5:11])   # prints characters from index 6 to 10
# this mainly used to get a substring from a given string

str2 = "shivam das"
print(str2[7:len(str2)])  # prints characters from index 7 to end of the string