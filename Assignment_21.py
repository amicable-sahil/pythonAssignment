#Q1:  -------------------- Recursive Function to Print N numbers  --------------------
def printNumbers(n):
    if n>0:
        printNumbers(n-1), print(n, end=" ")

printNumbers(10)


#Q2:  -------------------- Recursive Function to Print N reverse numbers  --------------------
def printNumbers(n):
    if n > 0:
        print(n, end=" "), printNumbers(n-1)

printNumbers(10)


#Q3:  -------------------- Recursive Function to Print N odd numbers  --------------------
def printNumbers(n):
    if n > 0:
        printNumbers(n-1), print(2*n-1, end=" ")

printNumbers(10)


#Q4:  -------------------- Recursive Function to Print N odd reverse numbers  --------------------
def printNumbers(n):
    if n > 0:
        print(2*n-1, end=" "), printNumbers(n-1)

printNumbers(10)


#Q5:  -------------------- Recursive Function to Print N even numbers  --------------------
def printNumbers(n):
    if n > 0:
        printNumbers(n-1), print(2*n, end=" ")

printNumbers(10)


#Q6:  -------------------- Recursive Function to Print N everse even numbers  --------------------
def printNumbers(n):
    if n > 0:
        print(2*n, end=" "), printNumbers(n-1) 

printNumbers(10)


#Q7:  -------------------- Recursive Function to Print square of N numbers  --------------------
def printNumbers(n):
    if n>0:
        printNumbers(n-1), print(n*n, end=" ")

printNumbers(10)


#Q8:  -------------------- Recursive Function to Print cubes of N numbers  --------------------
def printNumbers(n):
    if n>0:
        printNumbers(n-1), print(n**3, end=" ")

printNumbers(10)



#Q9:  -------------------- Recursive Function to Print N multiples  --------------------
def printNumbers(n,tn):
    i = n
    if n > 0:
        printNumbers(n-1, tn), print(tn*n, end=" ")

printNumbers(8,8)
# It would be more better it I pass only one argument, but I still not found a way to do this


#Q10:  -------------------- Recursive Function to reverse a number  --------------------
def printNumbers(n):
    strNum = str(n)
    l = len(strNum)
    if len(strNum) == 1:
        print(n)
    else:
        print(int(strNum[l-1]), end="")
        strNum =  strNum[0:l-1]
        n = int(strNum)
        printNumbers(n)

printNumbers(1065165)
printNumbers(8)
printNumbers(1158154)
