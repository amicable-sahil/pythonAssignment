#Q1:  -------------------- Recursive Function to Print sum of N numbers  --------------------
def sumOf_N_numbers(n):
    if n == 1:
        return 1
    return sumOf_N_numbers(n-1) + n

print("Sum of numbers is:", sumOf_N_numbers(10))


#Q2:  -------------------- Recursive Function to Print sum of N odd numbers  --------------------
def sumOf_N_odds(n):
    if n == 1:
        return 1
    return sumOf_N_odds(n-1) + 2*n-1

print("Sum of n odd numbers is:", sumOf_N_odds(5))


#Q3:  -------------------- Recursive Function to Print sum of N even numbers  --------------------
def sumOf_N_evens(n):
    if n == 1:
        return 2
    return sumOf_N_evens(n-1) + 2*n

print("Sum of n even numbers is:", sumOf_N_evens(5))


#Q4:  -------------------- Recursive Function to Print square sum of N numbers  --------------------
def sumOf_N_squares(n):
    if n == 1:
        return 1
    return sumOf_N_squares(n-1) + n*n

print("Sum of square of n odd numbers is:", sumOf_N_squares(5))


#Q5:  -------------------- Recursive Function to Print cubes sum of N numbers  --------------------
def sumOf_N_cubes(n):
    if n == 1:
        return 1
    return sumOf_N_cubes(n-1) + n*n*n

print("Sum ofcubes of n odd numbers is:", sumOf_N_cubes(5))


#Q6:  -------------------- Recursive Function to Print factorial of numbers  --------------------
def factN(n):
    if n == 1:
        return 1
    return factN(n-1) * n

print("Sum of n odd numbers is:", factN(5))


#Q7:  -------------------- Recursive Function to sum digits of a numbers  --------------------
def sum_of_digits(n):
    s1 = str(n)
    l = len(s1)
    if l == 1:
        return n
    else:
        i = int(s1[l-1])
        s1 = s1[0:l-1]
        n = int(s1)
    return sum_of_digits(n) + i

print("Sum of given digits are", sum_of_digits(100452))
print("Sum of given digits are", sum_of_digits(2))


#Q8:  -------------------- Recursive Function for Decimal to Binary  --------------------
def decimalToBinary(n):
    if n == 1:
        print(1, end="")
    else:
        x = (n % 2)
        q = int(n/2)
        n = q
        decimalToBinary(n), print(x, end="")

decimalToBinary(23)
print()

#Q9:  -------------------- Recursive Function for Decimal to Octal  --------------------
def decimalToOctal(n):
    if n > 0:
        x = (n % 8)
        q = int(n/8)
        n = q
        decimalToOctal(n), print(x, end="")


decimalToOctal(23)
print()


#Q10:  -------------------- Recursive Function to sum digits of a numbers  --------------------
def favSeries(n):
    a,b = 0,1
    while n>0:
        print(a, end=" ")
        a,b = b, a+b
        n -=1
    
favSeries(10)
# I still don't understand that how can i make it recursive ?


