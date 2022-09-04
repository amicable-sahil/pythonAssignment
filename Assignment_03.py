# Q1:
x = 14
y = str(x)
print("Value of y is: " + y)
print("Type of x is: ", type(x))
print("Type of y is: ", type(y))

# Q2:
myData = "m"
myUnicode = ord(myData)
print("The unicode of", myData, "is:", myUnicode)

# Q3:
myData = 100
myCharacter = chr(myData)
print("The character for", myData, "is:", myCharacter)

# Q4:
myData = 45
binaryNumber = bin(myData)
print("The binary number of", myData, "is:", binaryNumber)

#Q5:
myNumber = 55
octalNumber = oct(myNumber)
print("The Octal value of a number '", myNumber, "' is: ", octalNumber, sep="")

#Q6:
myNumber = 48
hexaNumber = hex(myNumber)
print("The hexa value of a number '", myNumber, "' is: ", hexaNumber, sep="")

#Q7:
bn = 1100101
binaryNumber = 0b1100101
print("The value of binary number",bn,"in decimal is:",binaryNumber)

#Q8:
hn = "2F"
hexaNumber = 0x2F
octNumber = oct(hexaNumber)
print("The value of hexa number",hn,"in octal is:",octalNumber)

#Q9:
on = 125
octaNumber = 0o125
binNumber = bin(octaNumber)
print("The value of octa number",on,"in banary is:",binNumber)

#Q10:
x = 0o25
y = 0x39
z = x + y
print(bin(z))