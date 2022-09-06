#Q1:--------------------------------------------------------------------
num = input("Enter a number ")  # Here I am getting number as a string
b = ""
for a in num:
    b = a + b
print(int(b))


#Q2:--------------------------------------------------------------------
num = int(input("Enter a number ")) 
for a in range(2, 10):
    if a != num and num%a == 0:
        print("Number is not prime")
        break
else:
    print("Prime")

#Q3:--------------------------------------------------------------------
i = 2
while i<=100:
    for a in range(2, 10):
        if i != a and i%a == 0:
            break
    else:
            print(i, end=" ")
    i +=1


# This program is for all non prime numbers
i = 2
while i<=100:
    for a in range(2, 10):
        if i != a and i%a == 0:
            print(i, end=" ")
            break
    i +=1
    


#Q4:--------------------------------------------------------------------
a = int(input("Enter initial number "))
b = int(input("Enter end number "))
while a<=b:
    for i in range(2, 10):
        if a != i and a%i ==0:
            break
    else:
        print(a, end=" ")
    a +=1


#Q5:--------------------------------------------------------------------
a = int(input("Enter initial number "))
b = ""
while b != "Prime":
    a += 1
    for i in range(2, 10):
        if a != i and a%i == 0:
            break
    else:
        b = "Prime"
        print("Next prime number is", a)


#Q6:--------------------------------------------------------------------
n = int(input("Enter a number "))
z = 1
i = 2
while z<=n:
    for a in range(2, 10):
        if i != a and i%a == 0:
            break
    else:
        print(i, end=" ")
        z += 1
    i +=1


#Q7:--------------------------------------------------------------------
a = int(input("Enter first number "))
b = int(input("Enter second number "))

for z in range(2, 10):
    if a%z ==0 and b%z ==0:
        print(a, "and", b, "are not co prime numbers")
        break
else:
    print(a,"and",b,"are co prime numbers")

#Q8:--------------------------------------------------------------------
a = 0
b = 1
i = 1
n = int(input("Enter a number "))
print(a, b, end=" ")
while i<n-1:
    c = a+b
    a = b
    b = c
    print(c, end=" ")
    i +=1

#Q9:--------------------------------------------------------------------
a = 2
b = 2
n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
z1 = n1
z2 = n2
while n1 != n2:
    if n1> n2:
        n2 = z2 * a
        a +=1
    else:
        n1 = z1 * b
        b +=1
print("LCM is:", n2)


#Q10:--------------------------------------------------------------------
n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
if n1>n2:
    while n1%n2 != 0:
        if n1%n2 == 0:
            print(n2, "is HCF")
        else:
            n2 = n1%n2
            n1 = n2
        print(n2, "is HCF")
elif n2>n1:
    while n2 % n1 != 0:
        if n2 % n1 == 0:
            print(n1, "is HCF")
        else:
            n1 = n2 % n1
            n2 = n1
        print(n1, "is HCF")

else:
    print("HCF is", n1)