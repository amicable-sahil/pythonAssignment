#Q1:  -------------------- access elements using Iter and Next method  --------------------
s1 = {12,15,56,24,35,74}
itr = iter(s1)
n = len(s1)
while n>0:
    print(next(itr), end=" ")
    n -=1


#Q2:  -------------------- Generator to produce n Odd numbers  --------------------
def nOddNumbers(n):
    i = 1
    while n:
        yield i
        i +=2
        n -=1
    
[print(e, end=" ") for e in nOddNumbers(10)]
print()
for e in nOddNumbers(int(input("Enter a number "))):
    print(e, end=" ")


#Q3:  -------------------- Generator to produce n Even numbers  --------------------
def nEvenNumbers(n):
    x = 2
    while n:
        yield x
        x +=2
        n -=1

for e in nEvenNumbers(int(input("Enter a number "))):
    print(e, end=" ")


#Q4:  -------------------- Generator to produce squares of N numbers  --------------------
def squareNumbers(n):
    i = 1
    while n:
        yield i*i
        i +=1
        n -=1

for e in squareNumbers(int(input("Enter a number "))):
    print(e, end=" ")


#Q5:  -------------------- Generator to produce fibonacci series of N numbers  --------------------
def fibSeries(n):
    a,b = 0,1
    while n:
        yield a
        a,b = b, a+b
        n -=1

for e in fibSeries(int(input("Enter a number "))):
    print(e, end=" ")


#Q6:  -------------------- Generator to produce fibonacci series of N numbers  --------------------
def primeNumbers(n):
    x = 2
    while n:
        for i in range(2,x):
            if x%i == 0:
                break
        else:
            yield x
            n -= 1
        x +=1
        

for e in primeNumbers(10):
    print(e, end=" ") 


#Q7:  -------------------- Generator to produce endless fibonacci series  --------------------
def endlessFib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

itr = endlessFib()
print("First fibonacci number is:",next(itr))
fib_list = [0]
while True:
    ans = input("Do you want next fibonacci number: [y/n] ")
    if ans == "y":
        x = next(itr)
        print(x)
        fib_list.append(x)
    else:
        print(fib_list)
        break


#Q8:  -------------------- Generator to produce endless prime numbers  --------------------
def endlessPrimeNumbers():
    x = 2
    while True:
        for i in range(2, x):
            if x%i == 0:
                break
        else:
            yield x
        x +=1

it = endlessPrimeNumbers() 
print("First prime number is:", next(it))
prime_list = [2]  
while True: 
    ans = input("Do you want next prime number [y/n]")
    if ans == "y":
        z = next(it)
        print(z)
        prime_list.append(z)
    else:
        print(prime_list)
        break


#Q9:  -------------------- Decorator function on triangle  --------------------
def deco_valid_triangle(peri_func):
    def check_valid_triangle(a,b,c):
        if a+b > c and a+c > b and b+c > a:
            peri_func(a,b,c)
        else:
            print("Given lengths are not valid for a triangle")
    return check_valid_triangle

@deco_valid_triangle
def perimeterOfTriangle(a,b,c):
    d = a+b+c
    print("The perimeter of triangle is:", d)

perimeterOfTriangle(6,2,5)


#Q10:  -------------------- Decorator function for HCF  --------------------
def decor_co_prime(hcf_func):
    def check_co_prime(a,b):
            for r in range(2, 10):
                if a%r ==0 and b%r == 0:
                    print("Numbers are not co-prime")
                    break
            else:
                print("Numbers are co-prime")
            hcf_func(a,b)

    return check_co_prime

@decor_co_prime
def hcf(a,b):
    if a<b:
        while b%a:
            r = b%a
            b = a
            a = r
        else:
            print("HCF:", a)
    else:
        while a%b:
            r = a%b
            a = b
            b = r
        else:
            print("HCF is:", b)

x = hcf(4,6)