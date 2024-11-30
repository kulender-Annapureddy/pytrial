# many values to multivariables
# x, y, z = 1, 2, 3
# print(x,y,z)

# one value to multivariables
# x= y= z= 2
# print(x)

# unpack a collection
# car = ["ford", "kia", "tata"]
# x, y, z = car
# print(car, x)

# Python Output variables
# print() => print function is used to output variables
# x = "python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = 5
# y =  "python"
# print(x, y)

# Python - Global variables

# x = "hello world"

# def myfunc():
#     global x
#     x = "hey, How you doing"
#     print(x + "!")

# myfunc()
# print(x)

# Data Types
# text Type => string,
# Numeric Types => int, float, complex,
# Sequence Types = > list, tuple, range,
# Mapping Types => dictionary,
# Set Types => set, frozenSet
# Boolean Types => bool,
# Binary Types => bytes, bytearray, memoryview,
# None Type => NoneType. 

# import random

# random_number = random.randint(1,10)
# print(f"randomm number: {random_number}")

# a =""" write something that comes to your 
# mind and display the output using the print
# method."""
# print(a)


# a = "hello, world!   "
# b = "KULENDER"
# # for x in a:
# #     print(x)
# print(len(a))
# print("hello" in a )
# print(a[1:3])
# print(a.upper())
# print(b.lower())
# print(a.strip())
# print(b.replace("KULENDER", "HARI"))
# print(b)
# print(a.split(" "))

# age = 3
# txt = f"hello world {age}"
# print(txt)

# txt = "we are the so called \"avengers\" in the marvel theme"
# print(txt)

# # String Methods
# txt ="for only {price:.2f} dollars"
# str = "Kulender"
# txt1 = "KULENDER 12"
# num = "123.4"
# print(str.capitalize())
# print(str.casefold())
# print(str.center(10))
# print(str.count("e"))
# print(str.encode())
# print(str.endswith("r"))
# print(str.find("r"))
# print(txt.format(price = 49))
# print(str.index("l"))
# print(txt1.isalnum())
# print(txt1.isascii())
# print(str.isidentifier())
# print(num.isdecimal())

# LIST
# => lists are used to store multiple items
# =>lists are stored in square brackets
# =>lists are mutable
# =>list are orderd list it will not change if we add new item to list it will be added to end of the list.
# =>list have a duplicated items and it allows it.
# =>lists can be any data type and also can different data types.
# =>list has constructor method 

thisList = ["ki", "ka", "ra"]
thisList2 =[1, 3, 4, 5, 6]
thisList3 = list(("red", 1, True)) #constructor method using key word list
print(thisList)
print(len(thisList))
print(type(thisList2))
print(type(thisList3))
#accessing list items
print(thisList[1])
print(thisList[-1])

# Python colletions
# there are four collection of data types in python programming
# LIST => list is a collection which is ordered index and changable. allows duplicate members.
#TUPLE => tuple is a collection which ordered and unchangable, allows duplicate members.
#SET => set is a collection which is unorderd, unchangeable, and unindexed, no duplicate members.
#Dictionary is a collection which is orderdered ad changeable, no duplicate members.


