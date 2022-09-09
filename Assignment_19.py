#Q1:  -------------------- Function to Print "MySirG"  --------------------
def f1():
    print("MySirG")

f1()

#Q2:  -------------------- Function except two arg and Print in fn body  --------------------
def f1(a, b):
    print("a =",a, "b =", b)

f1(5, "Hello")


#Q3:  -------------------- Function that except unknown arguments  --------------------
def f1(*arg):
    print(arg)

f1(5, "Hello", 4.5, True, 9, 3+4j, "You can do this")


#Q4:  -------------------- Function that except kwyWord arguments  --------------------
def f1(a, b, c):
    print("a =",a, "b =", b, "c =", c)

f1(5, c="Hello", b=4.5)


#Q5:  -------------------- Function that except list arguments  --------------------
def f1(a):
    for i in a:
        print(i, end=" ")

f1([1,2,3,4,5])


#Q6:  -------------------- Function to find max of 4 nums  --------------------
def maxNum(a,b,c,d):
    print("Max number is", max(a,b,c,d))

maxNum(45,25,15,85)


#Q7:  -------------------- Function to sum list numbers  --------------------
def sumListNums(list):
    listSum = sum(list)
    print("Sum of list elements is:",listSum)

myList = [10,20,30,40,50]
sumListNums(myList)


#Q8:  -------------------- Function to multiply list numbers  --------------------
def productOfListNums(list):
    product = 1
    for e in list:
        product = product*e
    print("Product of list elements is:",product)

myList = [10,20,30,4,5]
productOfListNums(myList)


#Q9:  -------------------- Function to check given number is in range or not  --------------------
def checkNUmberInRange(num):
    rangeIs = range(10,100)
    print("In range") if num in rangeIs else print("Not in range")

checkNUmberInRange(55)
checkNUmberInRange(5)

#Q10:  -------------------- Function to check given number is Even or Odd  --------------------
def checkEvenOdd(num):
    print("Number is odd") if num%2 else print("Number is Even")

checkEvenOdd(55)
checkEvenOdd(558)
