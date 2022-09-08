#Q1:-------------------------------------------------------
number = int(input("Enter a Number: "))
number = number//10
print(number)

#Q2:-------------------------------------------------------
number = int(input("Enter a Number: "))
number = number%10
print(number)

#Q3:-------------------------------------------------------
variable_1 = input("Enter something: ")
variable_2 = input("Enter something: ")
temp = variable_1
variable_1 = variable_2
variable_2 = temp
print("Variable 1's new value: ", variable_1)
print("Variable 2's new value: ", variable_2)


#Q4:-------------------------------------------------------
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
print(x ** y)


#Q5:-------------------------------------------------------
number = int(input("Enter a three digit Number: "))
number = number//100
print(number)


#Q6:-------------------------------------------------------
number = int(input("Enter a three digit Number: "))
number = number//10
number = number%10
print(number)


#Q7:-------------------------------------------------------
number = int(input("Enter a three digit Number: "))
number = number%10
print(number)


#Q8:-------------------------------------------------------
s = "MySirG"
print("My" in s)

#Q9:-------------------------------------------------------
s = "MySirG"
print("My" not in s)

#Q10:-------------------------------------------------------
a = 5
b = 8
c = 5
print(a is b)
print(a is c)
print(a is not b)