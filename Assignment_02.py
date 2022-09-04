import datetime
from Assignment_01 import varOfAssignment1
import Assignment_01
import keyword

# Q1: We can add a single line comment using '#'


print("Learn Python")

# Q2: We can add multiple lines comment using double qooute three times
"""
Line 1
Line 2
Line 3 
"""
myNumber = 55
myString = "Sahil"
myBoolean = True
myFloatNumber = 4.5
print(myNumber, myString, myBoolean, myFloatNumber, sep="\n")

# Q3:
aNumber = 137
aString = "MySirG"
aBoolean = False
aFloat = 11.10
anImaginaryNumber = 5 + 10j
anEmail = "sahil@gmail.com"
print(aNumber, aString, aBoolean, aFloat, anImaginaryNumber, anEmail, sep="\n")

# Q4:
a = 55
b = 55
print(id(a))
print(id(b))
# Here is an intresting thing, the ID of both variables are same.

# Q5:
a = 1447
b = "Learn Python"
c = 14.25
d = True
e = 55+45j
print(a, id(a), type(a), sep=" / ")
print(b, id(b), type(b), sep=" / ")
print(c, id(c), type(c), sep=" / ")
print(d, id(d), type(d), sep=" / ")
print(e, id(e), type(e), sep=" / ")


# Q6:
# Here I use [ import keyword ] to run this
print(keyword.kwlist)

# Q7: I use [ help('keywords') ] in IDLE shell and it runs fine


# Q8: Here I'll import a variable from a module (01_Assignment)
# Here I use [ import Assignment_01 ] to run this
print(Assignment_01.varOfAssignment1)

# Here I use [ from Assignment_01 import varOfAssignment1 ] to run this
print(varOfAssignment1)


# Q9:
""" There are three keywords which are used as data in python
    1. True
    2. False
    3. None
"""

# Q10:
# Here I use [ import datetime ] to run this
dt = datetime.datetime.now()
print("Today's date is:-> " + "[" + dt.strftime("%d"), dt.strftime("%m"), dt.strftime("%y") + "]", sep="-")
print("and time is:-> [" + dt.strftime("%I"), dt.strftime("%M") + " " + dt.strftime("%p") + "]", sep=":")
# method strftime() takes a parameter 'format' to specify the format
