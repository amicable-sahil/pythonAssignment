#Q1:--------------------------------------------------------------------
n = int(input("Enter a number "))
i = 1
s = 0
while i<=n:
    s = s + i
    i +=1
print("The sum of n natural numbers is", s)

#Q2:--------------------------------------------------------------------
n = int(input("Enter a number "))
i = 1
s = 0
while i<=n:
    s = s + i**2
    i +=1
print("The sum of square ofn natural numbers is", s)

#Q3:--------------------------------------------------------------------
n = int(input("Enter a number "))
i = 1
s = 0
while i <= n:
    s = s + i**3
    i += 1
print("The sum of cubes of n natural numbers is", s)


#Q4:--------------------------------------------------------------------
n = int(input("Enter a number "))
i = 1
s = 0
while i <= 2*n:
    s = s + i**2
    i += 2
print("The square sum of odd n natural numbers is", s)


#Q6:--------------------------------------------------------------------
n = int(input("Enter a number "))
s = 1
while n>1:
    s = s*n
    n -= 1
print("The factorial n natural numbers is", s)


#Q7:--------------------------------------------------------------------
n = int(input("Enter a number "))
i = 0
for a in str(n):
    i = i + 1
print("Total digits are", i)


#Q8:--------------------------------------------------------------------
n = int(input("Enter a number "))
i = 0
for a in str(n):
    i = i + int(a)
print("The sum of digits are", i)


#Q9:--------------------------------------------------------------------
n = int(input("Enter a number "))
rem =""
while n > 0:
    r = n%2
    q = int(n/2)
    rem = rem + str(r)
    n = q
print(rem[::-1])


#Q10:--------------------------------------------------------------------
n = int(input("Enter a number "))
remainder = ""
while n > 0:
    r = n%8
    q = int(n/8)
    remainder = remainder + str(r)
    n = q
print(remainder[::-1])
